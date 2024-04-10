def registrera_student(namn, ålder, kurser):
    student = {"namn": namn, "ålder": ålder, "kurser": kurser}
    return student


def visa_student(student):
    print(f"Namn: {student['namn']}")
    print(f"Ålder: {student['ålder']}")
    print("Kurser:")
    for kurs in student['kurser']:
        print(f"- {kurs}")

def uppdatera_student_kurser(student, nya_kurser):
    student['kurser'] += nya_kurser


def main():
    student1 = registrera_student("Alice", 20, ["Python- programmering", "Databasdesign"])
    visa_student(student1)
    student2 = registrera_student("Bob", 22, ["Python- programmering"])
    visa_student(student2)
    uppdatera_student_kurser(student2, ["Databasdesign"])
    visa_student(student1)
    visa_student(student2)


if __name__ == '__main__':
    main()