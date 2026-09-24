class AssignmentSubmission:
    def __init__(self, student_name, student_id, assignment_title, due_date):
        self.student_name = student_name
        self.student_id = student_id
        self._assignment_title = assignment_title
        self._due_date = due_date
        self.__is_submitted = False
        self.__grade = None
        self.__submitted_files = []

    def __validate_grade(self, score):
        if score < 0 or score > 100:
            raise ValueError("Grade must be between 0 and 100")

    def __check_submission_status(self):
        return self.__is_submitted

    def __duplicate(self, filename: str):
        if filename in self.__submitted_files:
            print(f"--> [Success] '{filename}' is already attached!")
            return True
        return False

    def add_file(self, filename):
        if self.__duplicate(filename):
            return
        self.__submitted_files.append(filename)
        self.__is_submitted = True
        print(f"--> [Success] {self.student_name} attached '{filename}'. Total files: {len(self.__submitted_files)}")

    def remove_file(self, filename):
        if self.__grade is not None:
            print(f"--> [Warning] {self.student_name} cannot remove files. Assignment already graded.")
            return
        if filename in self.__submitted_files:
            self.__submitted_files.remove(filename)
            if not self.__submitted_files:
                self.__is_submitted = False
            print(f"--> [Success] {self.student_name} removed '{filename}'.")
        else:
            print(f"File '{filename}' not found in the submission.")

    def assign_grade(self, score: float):
        if not self.__check_submission_status():
            raise ValueError(f"--> [Error] Cannot grade. No files submitted for {self.student_name}")
        self.__validate_grade(score)
        self.__grade = score
        print(f"--> [Success] Grade {score} officially assigned to {self.student_name}.")

    def get_grade(self):
        return self.__grade

    def view_files(self):
        return ", ".join(self.__submitted_files)

    def get_detailed_report(self):
        status = "Submitted" if self.__is_submitted else "Not Submitted"
        grade = self.__grade if self.__grade is not None else "Not Graded"
        return (f"Student: {self.student_name}, ID: {self.student_id}, "
                f"Assignment: {self._assignment_title}, Due Date: {self._due_date}, "
                f"Status: {status}, Grade: {grade}")

    def get_status_report(self):
        status = f"Submitted ({len(self.__submitted_files)} files)" if self.__is_submitted else "Missing"
        grade = self.__grade if self.__grade is not None else "Not Graded"
        return f"ID: {self.student_id} | Name: {self.student_name:<15} | Status: {status:<19} | Grade: {grade}"

student1 = AssignmentSubmission(student_name="Alex Gonzaga", student_id="pshs-1090-x", assignment_title="CS-101", due_date="2029-10-01")
student2 = AssignmentSubmission(student_name="Adelle", student_id="pshs-1020-x", assignment_title="CS-101", due_date="2029-10-01")
student3 = AssignmentSubmission(student_name="Juan Dela Cruz", student_id="pshs-1033-x", assignment_title="CS-101", due_date="2029-10-01")
student4 = AssignmentSubmission(student_name="Maria Santos", student_id="pshs-1044-x", assignment_title="CS-101", due_date="2029-10-01")
student5 = AssignmentSubmission(student_name="Jose Reyes", student_id="pshs-1055-x", assignment_title="CS-101", due_date="2029-10-01")

print("--- INITIALIZING DROPBOX FOR STUDENTS ---")
student1 = AssignmentSubmission(student_name="Alex Gonzaga", student_id="pshs-1090-x", assignment_title="CS-101", due_date="2029-10-01")
student2 = AssignmentSubmission(student_name="Adelle", student_id="pshs-1020-x", assignment_title="CS-101", due_date="2029-10-01")
student3 = AssignmentSubmission(student_name="Juan Dela Cruz", student_id="pshs-1033-x", assignment_title="CS-101", due_date="2029-10-01")
student4 = AssignmentSubmission(student_name="Maria Santos", student_id="pshs-1044-x", assignment_title="CS-101", due_date="2029-10-01")
student5 = AssignmentSubmission(student_name="Jose Reyes", student_id="pshs-1055-x", assignment_title="CS-101", due_date="2029-10-01")
print()

print("--- TEST SCENARIO 1: Multiple Files via List ---")
student1.add_file("main.py")
student1.add_file("report.pdf")
student1.assign_grade(95)
print(f"Alex's Files: {student1.view_files()}\n")

print("--- TEST SCENARIO 2: Removing Files via List ---")
student2.add_file("wrong_homework.docx")
student2.remove_file("wrong_homework.docx")
student2.add_file("correct_project.py")
student2.assign_grade(88)
print(f"Adelle's Files: {student2.view_files()}\n")

print("--- TEST SCENARIO 3: Preventing Duplicate Files ---")
student3.add_file("script.py")
student3.add_file("script.py") # Should Trigger private duplicate check
print(f"Juan's Files: {student3.view_files()}\n")

print("--- TEST SCENARIO 4: Removing file after being graded ---")
student4.add_file("exam_answers.pdf")
student4.assign_grade(75)
student4.remove_file("exam_answers.pdf") # Blocked by grading status
print()

print("--- TEST SCENARIO 5: Empty list handling ---")
student5.add_file("draft.txt")
student5.remove_file("draft.txt")
try:
    student5.assign_grade(100) # Should fail because list is empty
except ValueError as error:
    print(error)
print()

print("--- FINAL SYSTEM REPORT ---")
print(student1.get_status_report())
print(student2.get_status_report())
print(student3.get_status_report())
print(student4.get_status_report())
print(student5.get_status_report())
