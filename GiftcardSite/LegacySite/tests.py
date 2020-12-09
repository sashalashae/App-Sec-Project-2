from django.test import TestCase
from django.test import Client
from LegacySite.views import use_card_view, gift_card_view, buy_card_view

# Create your tests here.


class TestPart1(TestCase):
    def test_xss(self):
        c = Client()
        out = c.get(
            "/buy/",
            {"director": '<script>alert("You have been hacked: XSS Style)</script>'},
        )
        assert out.status_code == 200
