from base import TestBase
from core.models.user import User

class TestUser(TestBase):

    def setUp(self):
        self.user = User("Igor", 25, "igo@ccc.ufcg.edu.br", "igornsa", "password")

    def test_creation(self):
        user = User("Igor", 25, "igo@ccc.ufcg.edu.br", "igornsa", "password")

        self.assertEqual(user.name, 'Igor')
        self.assertEqual(user.age, 25)
        self.assertEqual(user.email, 'igo@ccc.ufcg.edu.br')
        self.assertEqual(user.username, "igornsa")
        self.assertEqual(user.password, "password")
        self.assertNotEqual(user.name, "Olar")
        self.assertNotEqual(user.age, -1)
        self.assertNotEqual(user.email, "gmail@gmail.com")
        self.assertNotEqual(user.username, "rogihc")
        self.assertNotEqual(user.password, "!senha!")

    def test_setters(self):
        self.user.set_age(13)
        self.assertEqual(self.user.age, 13)
        self.assertNotEqual(self.user.age, 25)
        self.user.set_name("Ursula")
        self.assertNotEqual(self.user.name, 'Igor')
        self.assertEqual(self.user.name, 'Ursula')
        self.user.set_email("mail@bol.com.br")
        self.assertNotEqual(self.user.email, "igo@ccc.ufcg.edu.br")
        self.assertEqual(self.user.email, "mail@bol.com.br")
        self.user.set_password("******")
        self.assertNotEqual(self.user.password, "password")
        self.assertEqual(self.user.password, "******")

    def test_report(self):
        self.user.report_lost("Achei uma bolsa",
                              "Lorem Ipsum",
                              "Estojo",
                              "LCC1", "14/02/2017",
                              "1", None, "3331-2163")
        self.assertEqual(len(self.user.reports), 1)

        self.user.report_found("Achei uma bolsa",
                              "Lorem Ipsum",
                              "Estojo",
                              "LCC1", "14/02/2017",
                              "1", None, "3331-2163")

        self.assertEqual(len(self.user.reports), 2)