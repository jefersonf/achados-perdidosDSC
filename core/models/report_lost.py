from core.models.report import Report

class ReportLost(Report):

    def __init__(self, title, description, type, local, date, shift, photo, phone):
        super(ReportLost, self).__init__(title, description, type, local, date, shift, photo, phone)