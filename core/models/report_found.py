from core.models.report import Report

class ReportFound(Report):

    def __init__(self, title, description, type, local, date, shift, photo, phone):
        super(ReportFound, self).__init__(title, description, type, local, date, shift, photo, phone)