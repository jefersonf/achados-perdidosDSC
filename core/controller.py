import core.utils as utils

from core.models.user import User

class Controller(object):
    def __init__(self):
        self.users = []

    def all_reports(self):
        reports = []
        for u in self.users:
            reports.append(u.reports)

        return sorted(reports, key=lambda x: x.date,  reverse=True)

    def register_user(self, name, age, email, username, password):
        if utils.validate_email(email) and utils.check_user(username, self.users):
            self.users.append(User(name, age, email, username, password))
            return True
        return False

    def report_lost(self, username, title, description, type, local, date, shift, photo, phone):
        user = self._get_user(username)
        if user:
            return user.report_lost(title, description, type, local, date, shift, photo, phone)
        return None

    def report_found(self, username, title, description, type, local, date, shift, photo, phone):
        user = self._get_user(username)
        if user:
            return user.report_found(title, description, type, local, date, shift, photo, phone)
        return None

    def _get_user(self, username):
        for u in self.users:
            if username == u.username:
                return u
        return None
