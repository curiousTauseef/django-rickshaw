from rickshaw.models import Rickshaw, Cargo
from django.db import IntegrityError
from django.conf import settings
from rickshaw.errors import RickshawCargoError


class RickshawService:

    rickshaw = None

    def __init__(self, request):
        try:
            if not request.user.is_anonymous:
                self.rickshaw = Rickshaw.wheels.get(driver=request.user.id)
            else:
                rickshaw = Rickshaw.wheels.filter(session=request.session.session_key)
                if rickshaw.count() > 1:
                    self.rickshaw = rickshaw.first()
                    raise RickshawCargoError("Multiple Rickshaw exists for this id {0}".format(request.session.session_key))
                else:
                    self.rickshaw = rickshaw.first()
        except Rickshaw.DoesNotExist:
            self.rickshaw = self.build_rickshaw(request)

    def build_rickshaw(self, request):
        if not request.user.is_anonymous:
            r = Rickshaw(driver=request.user, session=request.session.session_key)
        else:
            r = Rickshaw(session=request.session.session_key)
        r.save()
        request.session["rickshaw"] = r.uuid.__str__()
        return self.rickshaw

    def fetch_rickshaw(self):
        try:
            return self.rickshaw
        except Rickshaw.DoesNotExist:
            raise RickshawCargoError("Rickshaw Does not Exist")

    def add_cargo(self, product, quantity=1):
        try:
            cargo = Cargo.hold.get(
                rickshaw=self.rickshaw,
                product=product
            )
        except Cargo.DoesNotExist:
            cargo = Cargo(
                rickshaw=self.rickshaw,
                product=product,
                quantity=quantity
            )
            cargo.save()
        else:
            self.update_cargo(product, quantity)

    def update_cargo(self, product, quantity=1):
        try:
            cargo = Cargo.hold.get(
                rickshaw=self.rickshaw,
                product=product
            )
        except Cargo.DoesNotExist:
            raise RickshawCargoError("Cargo Hold does not exists")
        else:
            if quantity == 0:
                cargo.delete()
            else:
                cargo.quantity = quantity
                cargo.save()

    def clear_cargo_hold(self):
        try:
            cargo = Cargo.hold.filter(rickshaw=self.rickshaw)
            for box in cargo:
                box.delete()
            return cargo
        except Cargo.DoesNotExist:
            return RickshawCargoError("Cargo does not exist")

    def cargo_hold_count(self):
        try:
            return Cargo.hold.filter(rickshaw=self.rickshaw).count()
        except Cargo.DoesNotExist:
            return RickshawCargoError("Cargo does not exist")

    def cargo_value(self):
        try:
            cargo = Cargo.hold.filter(rickshaw=self.rickshaw)
            value = 0
            for box in cargo:
                value = value + box.price
            return value
        except Cargo.DoesNotExist:
            return RickshawCargoError("Cargo does not exist")

    def cargo_hold(self):
        try:
            return Cargo.hold.filter(rickshaw=self.rickshaw)
        except Cargo.DoesNotExist:
            return RickshawCargoError("Cargo does not exist")
