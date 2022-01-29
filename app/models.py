from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from .managers import CustomUserManager


class Plan(models.Model):
    name=models.CharField(max_length=20,unique=True)
    def __str__(self):
        return  self.name

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    CompanyName = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    Plan = models.ForeignKey(Plan,on_delete=models.CASCADE,null=True)
    BillingDetails = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=20)
    wesite_url=models.CharField(max_length=200)
    is_staff = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

from django.conf import settings
class Product(models.Model):
    name = models.CharField(max_length=20)
    sr_number = models.CharField(max_length=50)
    usr = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    Qr_code = models.FileField(null=True,unique=True)

    def __str__(self):
        return self.name


class lang(models.Model):
    name=models.CharField(max_length=100)
    usr=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class language(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    language = models.ForeignKey(lang,on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=30,null=True)
    txt = models.CharField(max_length=300,null=True)
    image = models.ImageField(null=True)
    video=models.CharField(max_length=300,null=True)
    # video = models.FileField(upload_to='videos_uploaded', null=True, validators=[
    #     FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
