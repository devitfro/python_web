import json

class StudentDatabase:
    def __init__(self, filename):
        self.filename = filename

    def add_student(self, student):
        data = self.read_students()
        data.append({
            "name": student.name,
            "age": student.age,
            "grades": student.grades
        })

        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def read_students(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except:
            return []

    def find_student(self, name):
        data = self.read_students()
        for s in data:
            if s["name"].lower() == name.lower():
                return s
        return "Не знайдено"