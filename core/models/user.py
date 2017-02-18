from core.models.report_lost import ReportLost
from core.models.report_found import ReportFound

class User:

    def __init__(self, name, age, email, username, password):
        self.name = name
        self.age = age
        self.email = email
        self.username = username
        self.password = password
        self.reports = []

    def report_lost(self, title, description, type, local, date, shift, photo, phone):
        report = ReportLost(title, description, type, local, date, shift, photo, phone)
        self.reports.append(report)
        return report

    def report_found(self, title, description, type, local, date, shift, photo, phone):
        report = ReportFound(title, description, type, local, date, shift, photo, phone)
        self.reports.append(report)
        return report

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_email(self, email):
        self.email = email

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def get_atrributes(self):
        return "%s %s %s %s" % (self.name, self.age, self.email, self.password)

