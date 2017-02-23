import core.utils as utils

from core.models.user import User

class Controller(object):
    def __init__(self):
        self.users = []

    def all_reports(self):
        reports = []
        for u in self.users:
            for r in u.reports:
                reports.append(r)
        if len(reports) == 0:
            return reports
        return reports.sort(key=lambda x: x.date,  reverse=True)

    def register_user(self, name, age, email, username, password):
        if utils.validate_email(email) and utils.check_user(username, self.users):
            self.users.append(User(name, age, email, username, password))
            return True
        raise Exception("Invalid e-mail")

    def report_lost(self, username, title, description, type, local, date, shift, photo, phone):
        user = self._get_user(username)
        if user:
            return user.report_lost(title, description, type, local, date, shift, photo, phone)
        raise Exception("Invalid user")

    def report_found(self, username, title, description, type, local, date, shift, photo, phone):
        user = self._get_user(username)
        if user:
            return user.report_found(title, description, type, local, date, shift, photo, phone)
        raise Exception("Invalid user")

    def _get_user(self, username):
        for u in self.users:
            if username == u.username:
                return u
        raise Exception("Invalid username")
