from django.db.models import IntegerChoices


class GenderChoices(IntegerChoices):
    """(
        (1, 'Male',),
        (2, 'Female',),
        (3, 'Other1',),
        )
    """
    Male = 1
    Female = 2
    Other = 3


class CarTypeChoices(IntegerChoices):
    """(
        (1, 'Sedan',),
        (2, 'Jeep',),
        (3, 'Taxi',),
        (4, 'MiniVan',),
        )
    """
    Sedan = 1
    Jeep = 2
    Taxi = 3
    MiniVan = 4
