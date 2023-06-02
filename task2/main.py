from doctor import Doctor
from director import Director
from student import Student
from worker import Worker


def main():
    doc = Doctor("Watson", 55, True, 45)
    student = Student("Alex", 20, True, 10)
    director = Director("Trueman", 60, True, 80)
    worker = Worker("Volodya", 45, True, 2500)

    print(doc)
    doc.can_cure()

    print(student)
    student.can_study()

    print(director)
    director.can_run()

    print(worker)
    worker.can_work()

if __name__ == "__main__":
    main()
