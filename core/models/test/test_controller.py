from base import TestBase
from core.controller import Controller

import datetime

class TestUser(TestBase):

    def setUp(self):
        self.controller = Controller()

    def test_register(self):
        self.assertEquals(len(self.controller.users), 0)
        self.controller.register_user("Igor Natanael",
                                      15, "igor@ccc.ufcg.edu.br",
                                      "igor", "senha")
        self.assertEquals(len(self.controller.users), 1)

        try:
            self.controller.register_user("Igor Natanael",
                                          15, "igor@gmail.com",
                                          "igor", "senha")
        except Exception as e:
            self.assertEquals(e.message, "Invalid e-mail")


    def test_report_found(self):
        self.assertEquals(len(self.controller.all_reports()), 0)
        self.assertEquals(self.controller.all_reports(), [])
        self.controller.register_user("Igor Natanael",
                                      15, "igor@ccc.ufcg.edu.br",
                                      "igor", "senha")
        self.controller.report_found('igor', 'Achei', 'loremipsym',
                                     'Estojo', 'LCC1', datetime.datetime.now(),
                                     3, None, '3333-5555')
        self.assertEquals(len(self.controller.all_reports()), 1)

        try:
            self.controller.report_found('inexistente', 'Achei', 'loremipsym',
                                         'Estojo', 'LCC1', datetime.datetime.now(),
                                         3, None, '3333-5555')
        except Exception as e:
            self.assertEquals(e.message, "Invalid username")

    def test_report_lost(self):
        self.assertEquals(len(self.controller.all_reports()), 0)
        self.assertEquals(self.controller.all_reports(), [])
        self.controller.register_user("Igor Natanael",
                                      15, "igor@ccc.ufcg.edu.br",
                                      "igor", "senha")
        self.controller.report_lost('igor', 'Achei', 'loremipsym',
                                     'Estojo', 'LCC1', datetime.datetime.now(),
                                     3, None, '3333-5555')
        self.assertEquals(len(self.controller.all_reports()), 1)

        try:
            self.controller.report_lost('inexistente', 'Achei', 'loremipsym',
                                         'Estojo', 'LCC1', datetime.datetime.now(),
                                         3, None, '3333-5555')
        except Exception as e:
            self.assertEquals(e.message, "Invalid username")
