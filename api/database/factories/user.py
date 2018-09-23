
from factory.django import DjangoModelFactory


class UserFactory(DjangoModelFactory):
    class Meta:
        model = 'core.User'

    first_name = 'Rafael'
    last_name = 'Zarate Galvez'
    description = 'test'
    email_address = 'rafazrte@gmail.com'
    dob = '1995-09-18'
    

