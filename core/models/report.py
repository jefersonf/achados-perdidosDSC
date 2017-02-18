from abc import ABCMeta, abstractmethod

class Report:
    __metaclass__ = ABCMeta

    def __init__(self, title, description, type, local, date, shift, photo, phone):
        self.title = title
        self.description = description
        self.type = type
        self.local = local
        self.date = date
        self.shift = shift
        self.photo = photo
        self.phone = phone
        self.id = self.generate_id()
        self.solved = False

    def generate_id(self):
        return 0

    def set_title(self, title):
        self.title = title

    def set_description(self, description):
        self.description = description

    def set_type(self, type):
        self.type = type

    def set_local(self, local):
        self.local = local

    def set_date(self, date):
        self.date = date

    def set_shift(self, shift):
        self.shift = shift

    def set_photo(self, photo):
        self.photo = photo

    def set_phone(self, phone):
        self.phone = phone

    def set_solved(self, solved):
        self.solved = solved

    def get_attributes(self):
        return " %s %s %s %s %s %s %s %s %s" % (self.title, self.description, self.type,
                                               self.local, self.date, self.shift,
                                               self.photo, self.phone, self.solved)
