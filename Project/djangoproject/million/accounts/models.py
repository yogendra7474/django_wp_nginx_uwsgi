from django.db import models
# from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.hashers import (
    check_password, is_password_usable, make_password,
)
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils.crypto import get_random_string, salted_hmac




class UserManager(BaseUserManager):
    def create_user(self, email, is_verified=False, is_superuser=False,is_staff=True, is_active=True, is_admin=False, password=None, is_passwordok=False):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            # is_admin=True
            # password=password,

        )
        user.set_password(password)
        user.staff = is_staff
        user.active = is_active
        user.admin = is_admin
        user.verified = is_verified
        user.passwordok = is_passwordok
        user.save(using=self._db)
        return user



    def create_staffuser(self, email, password=None,):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            is_staff=True,
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password=None,**extra_fields):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True,
            is_active=True,
        )
        user.superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    superuser = models.BooleanField(default=False)
    passwordok = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    verified = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=[]
    

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_perms(self, perms, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def get_username(self):
        """Return the username for this User."""
        return self.email

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password

    def check_password(self, raw_password):
        """
        Return a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """
        def setter(raw_password):
            self.set_password(raw_password)
            # Password hash upgrades shouldn't be considered password changes.
            self._password = None
            self.save(update_fields=["password"])
        return check_password(raw_password, self.password, setter)

    def set_unusable_password(self):
        # Set a value that will never be a valid hash
        self.password = make_password(None)

    def get_session_auth_hash(self):
            """
            Return an HMAC of the password field.
            """
            key_salt = "django.contrib.auth.models.AbstractBaseUser.get_session_auth_hash"
            return salted_hmac(key_salt, self.password).hexdigest()
    def has_usable_password(self):
        """
        Return False if set_unusable_password() has been called for this user.
        """
        return is_password_usable(self.password)

    # def get_session_auth_hash(self):
    #     """
    #     Return an HMAC of the password field.
    #     """
    #     key_salt = "django.contrib.auth.models.AbstractBaseUser.get_session_auth_hash"
    #     return salted_hmac(key_salt, self.password).hexdigest()


    @property
    def is_verified(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.verified

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    @property
    def is_admin(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.admin

    @property
    def is_active(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.active

    @property
    def is_passwordok(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.passwordok

    @property
    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True

class GuestMail(models.Model):
    email=models.EmailField()
    active=models.BooleanField(default=True)
    update=models.DateTimeField(auto_now=True)
    timestamp=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
