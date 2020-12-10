import json
from unittest import TestCase
from django.test import Client
from django.urls import reverse, resolve
from LegacySite.views import login_view, use_card_view, gift_card_view, buy_card_view


# Create your tests here.


class TestPart1(TestCase):
    def setUp(self):
        self.client = Client()
        self.gift_url = reverse("Gift a Card")
        self.login_url = reverse("Login")
        self.use_url = reverse("Use a card")

    def test_gift_xss(self):
        response = self.client.get(
            self.gift_url, {"director": "<script>alert(1)</script>"}
        )
        self.assertEquals(response.status_code, 200)

    def test_gift_csrf(self):
        self.client.login(username="Hackerbae", password="Hackerbae")
        response = self.client.post(
            self.gift_url,
            {"username": "Hackerbae", "user": "Sasha123", "amount": "99135591"},
        )
        self.assertEquals(response.status_code, 200)

    def test_use_sqli(self):
        self.client.login(username="Hackerbae", password="Hackerbae")
        with open("part 1/sqlattack.gftcrd") as fdata:
            response = self.client.post(
                self.use_url,
                {
                    "card_supplied": "True",
                    "card_fname": "TestTestTest",
                    "card_data": fdata,
                },
            )
        self.assertEquals(response.status_code, 200)

    def test_command_injection(self):
        self.client.login(username="Hackerbae", password="Hackerbae")
        with open("part 1/newcard.gftcrd") as fdata:
            response = self.client.post(
                self.use_url,
                {
                    "card_supplied": "True",
                    "card_data": fdata,
                    "card_fname": ";ls;",
                },
            )
        self.assertEquals(response.status_code, 200)
