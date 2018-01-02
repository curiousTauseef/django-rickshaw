from django.db import IntegrityError


class RickshawCargoError(IntegrityError):
    pass