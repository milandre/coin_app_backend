"""CoinApp User models.

This file has the database models used
for user module.
"""

from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)
from django.core.validators import EmailValidator, RegexValidator
from django.contrib.auth.models import BaseUserManager

from django.contrib.auth.models import (
    BaseUserManager, 
    PermissionsMixin, 
    AbstractBaseUser
)

# Create your models here.

class ClientManager(BaseUserManager):
    """ClientManager

    Gives create_user and create_superuser to Client   
    """

    def create_user(self, email, password=None):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
    
        user = self.create_user(email,
            password=password
        )

        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class Client(AbstractBaseUser, PermissionsMixin):
    """Client model

    Client model base on AbstractUser    
    """

    email = models.EmailField(max_length=255, 
                              unique=True, 
                              db_index=True,
                              validators=[EmailValidator()])

    first_name = models.CharField(max_length=30,
                                  validators=[
                                    RegexValidator(
                                        regex='^[a-zA-Z]+$',
                                        message='Enter a valid name. This value only contains letters.',
                                        code='invalid_first_name'
                                    )
                                ])
    last_name = models.CharField(max_length=30,
                                 validators=[
                                    RegexValidator(
                                        regex='^[a-zA-Z]+$',
                                        message='Enter a valid name. This value only contains letters.',
                                        code='invalid_last_name'
                                    )
                                ])

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = ClientManager() 

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ()

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    @property
    def is_staff(self):
        # Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin    

    def __str__(self):
        return self.first_name + ' ' + self.last_name 

