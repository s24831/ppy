import smtplib
from email.mime.text import MIMEText


class Student:
    students = []

    def __init__(self, email: str, imie: str, nazwisko: str, punkty: float, ocena_koncowa=None, status=None):
        self.email = email
        self.imie = imie
        self.nazwsiko = nazwisko
        self.punkty = punkty
        self.ocena_koncowa = ocena_koncowa
        self.staus = status
        self.students.append(self)

    @classmethod
    def grade(cls) -> None:
        for student in cls.students:
            if not student.staus:
                if student.punkty <= 50:
                    student.ocena_koncowa = 2
                elif student.punkty <= 60:
                    student.ocena_koncowa = 3
                elif student.punkty <= 70:
                    student.ocena_koncowa = 3.5
                elif student.punkty <= 80:
                    student.ocena_koncowa = 4
                elif student.punkty <= 90:
                    student.ocena_koncowa = 4.5
                else:
                    student.ocena_koncowa = 5
            student.staus = 'GRADED'
        cls.save_to_file()

    @classmethod
    def add_new_student(cls, email: str, imie: str, nazwisko: str, punkty: float, ocena_koncowa=None, status=None):
        for s in cls.students:
            if s.email == email:
                return "email zajety"
        s = Student(email, imie, nazwisko, punkty, ocena_koncowa, status)
        cls.save_to_file()
        return s

    @classmethod
    def delete_student(cls, email: str):
        for i, s in enumerate(cls.students):
            if s.email == email:
                cls.students.pop(i)
        cls.save_to_file()

    @classmethod
    def send_email(cls, subject, body, sender, password):
        recipients = []
        for s in cls.students:
            if s.status != 'MAILED':
                s.status = 'MAILED'
                recipients.append(s.email)
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ', '.join(recipients)
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
        smtp_server.quit()
        cls.save_to_file()

    @classmethod
    def save_to_file(cls):
        with open(f".\students.txt", 'w') as file:
            for s in cls.students:
                file.write(f"{s}\n")

    def __repr__(self):
        return f"{self.email},{self.imie},{self.nazwsiko},{self.punkty},{self.ocena_koncowa},{self.staus}"
