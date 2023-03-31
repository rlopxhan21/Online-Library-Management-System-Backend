from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError(("The Email Field cannot be empty!"))
        
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
#     def create_superuser(self, email ,password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(email, password, **extra_fields)
    
# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     full_name = models.CharField(max_length=256)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
    

#     USERNAME_FIELD ='email'
#     REQUIRED_FIELDS = ["full_name"]

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email


# class User(AbstractUser):
#     # Override the 'username' field to make it non-unique
#     username = None

#     # Add any additional fields you need
#     age = models.PositiveIntegerField()
#     gender = models.CharField(max_length=10)

#     AbstractUser._meta.get_field('email')._unique = True
#     AbstractUser._meta.get_field('email').blank = False
#     AbstractUser._meta.get_field('email').null = False

#     # Update the REQUIRED_FIELDS to reflect the new required fields
#     EMAIL_FIELD = 'email'
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []