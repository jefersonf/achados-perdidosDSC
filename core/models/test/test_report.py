from base import TestBase
from core.models.report_lost import ReportLost
from core.models.report_found import ReportFound

from core.models.user import User

class TestUser(TestBase):

    def setUp(self):
        self.found = ReportFound("Achei uma bolsa",
                                  "Lorem Ipsum",
                                  "Estojo",
                                  "LCC1", "14/02/2017",
                                  "1", None, "3331-2163")

        self.lost = ReportLost("Achei uma coisa",
                              "Lorem Ipsum2",
                              "Roupa",
                              "LCC2", "15/02/2017",
                              "2", None, "3337-2163")

    def test_report_found(self):
        try:
            ReportFound(None,
                     "Lorem Ipsum2",
                     "Roupa",
                     "LCC2", "15/02/2017",
                     "2", None, "3337-2163")
        except Exception as e:
            self.assertEquals(e.message, "ERROR - Attributes missing")

        try:
            ReportFound("Bolseta",
                     None,
                     "Roupa",
                     "LCC2", "15/02/2017",
                     "2", None, "3337-2163")
        except Exception as e:
            self.assertEquals(e.message, "ERROR - Attributes missing")

        try:
            ReportFound("Bolseta",
                        "Lorem Ipsum2",
                        None,
                        "LCC2", "15/02/2017",
                        "2", None, "3337-2163")
        except Exception as e:
            self.assertEquals(e.message, "ERROR - Attributes missing")

        try:
            ReportFound("Bolseta",
                        "Lorem Ipsum2",
                        "Roupa",
                        None, "15/02/2017",
                        "2", None, "3337-2163")
        except Exception as e:
            self.assertEquals(e.message, "ERROR - Attributes missing")

        def test_report_lost(self):
            try:
                ReportLost(None,
                            "Lorem Ipsum2",
                            "Roupa",
                            "LCC2", "15/02/2017",
                            "2", None, "3337-2163")
            except Exception as e:
                self.assertEquals(e.message, "ERROR - Attributes missing")

            try:
                ReportLost("Bolseta",
                            None,
                            "Roupa",
                            "LCC2", "15/02/2017",
                            "2", None, "3337-2163")
            except Exception as e:
                self.assertEquals(e.message, "ERROR - Attributes missing")

            try:
                ReportLost("Bolseta",
                            "Lorem Ipsum2",
                            None,
                            "LCC2", "15/02/2017",
                            "2", None, "3337-2163")
            except Exception as e:
                self.assertEquals(e.message, "ERROR - Attributes missing")

            try:
                ReportLost("Bolseta",
                            "Lorem Ipsum2",
                            "Roupa",
                            None, "15/02/2017",
                            "2", None, "3337-2163")
            except Exception as e:
                self.assertEquals(e.message, "ERROR - Attributes missing")