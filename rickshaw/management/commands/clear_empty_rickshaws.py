from django.core.management.base import BaseCommand, CommandError
from django.contrib.sessions.models import Session
from rickshaw.models import *
from django.utils import timezone

class Command(BaseCommand):
    help = 'Clears the empty rickshaws based on session expiry to free up DB space and table size'

    def handle(self, *args, **options):
        rickshaws = Rickshaw.wheels.all()
        for rickshaw in rickshaws:
            try:
                session = Session.objects.get(session_key=rickshaw.session)
                print(session.expire_date)
                if timezone.now() > session.expire_date:
                    rickshaw.delete()
                else:
                    BaseCommand("Session Data is still valid")
            except Session.DoesNotExist:
                rickshaw.delete()
                raise CommandError("Session Data does not exist, deleting rickshaw")
