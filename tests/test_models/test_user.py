#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBaseModel
from models.user import User


class TestUser(TestBaseModel):
    """ Test for user"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value()
        new.first_name = "Abissa"
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value()
        new.last_name = "Paul"
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value()
        new.email = "p.rwagasana@alustudent.com"
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value()
        new.password = "123tunein"
        self.assertEqual(type(new.password), str)
