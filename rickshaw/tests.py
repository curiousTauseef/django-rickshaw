from django.test import TransactionTestCase, RequestFactory, Client
from django.contrib.auth.models import User, AnonymousUser
from rickshaw.shared.service import RickshawService
from django.contrib.sessions.middleware import SessionMiddleware
from .models import Cargo, Rickshaw
from rickshaw_example.models import Product
from django.conf import settings


class RickshawBaseTests(TransactionTestCase):

    """
    Tests for creating a rickshaw, adding cargo, updating cargo, removing cargo and emptying the rickshaw
    """

    rickshaw = None
    key = None
    product = None

    def setUp(self):
        self.client = Client()
        self.request = RequestFactory()
        self.request.user = AnonymousUser()
        self.request.session = self.client.session
        self.key = self.request.session.session_key

    def _build_get_rickshaw(self):
        try:
            rickshaw = Rickshaw(session=self.key)
            rickshaw.save()
            return rickshaw
        except Exception:
            rickshaw = Rickshaw.wheels.get(session=self.key)
            return rickshaw

    def _build_product(self):
        product = self.product(title="Test Product", description="Test Product", unit_price=19.99, stock=100)
        product.save()
        return product

    def test_build_rickshaw(self):
        rickshaw = self._build_get_rickshaw()
        stored = Rickshaw.wheels.get(session=self.key)
        self.assertEquals(rickshaw, stored)

    def test_add_cargo_to_rickshaw(self):
        rickshaw = self._build_get_rickshaw()
        product = self._build_product()
        cargo = Cargo(rickshaw=rickshaw, product=product, quantity=4)
        cargo.save()

        box_in_cargo = cargo.product

        self.assertEquals(box_in_cargo, product)
        self.assertEquals(cargo.price, product.unit_price * 4)

    def test_unload_cargo_from_rickshaw(self):
        rickshaw = self._build_get_rickshaw()
        product = self._build_product()
        cargo = Cargo(rickshaw=rickshaw, product=product, quantity=4)
        cargo.save()
        cargoes = Cargo.hold.filter(rickshaw=rickshaw)
        cargoes_count = cargoes.count()

        self.assertGreater(cargoes_count, 0)

        cargoes.delete()
        cargoes_count = cargoes.count()

        self.assertEquals(cargoes_count, 0)

    def test_amend_cargo_in_rickshaw(self):
        rickshaw = self._build_get_rickshaw()
        product = self._build_product()
        cargo = Cargo(rickshaw=rickshaw, product=product, quantity=4)
        cargo.save()

        edited_cargo = Cargo.hold.first()
        edited_cargo.quantity = 10
        edited_cargo.save()

        self.assertTrue(edited_cargo.quantity, cargo.quantity)
        self.assertGreater(edited_cargo.price, cargo.price)

    def _test_value_of_cargo(self):
        pass


class RickshawTests(RickshawBaseTests):

    """
        Extends from RickshawBaseTests for custom product model and method override if required
    """

    product = Product


