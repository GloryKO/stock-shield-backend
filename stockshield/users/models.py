from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model
from django.template.defaultfilters import slugify
from phone_field import PhoneField
import random
import string


class BusinessId(models.Model):
    id = models.SlugField(primary_key=True,unique=True)
    business_name = models.CharField(max_length=150)

    @classmethod
    def make_slug(cls,chars = string.ascii_lowercase + string.digits ):
        generated_slug = ''.join(random.choice(chars) for _ in range(6))
        slug = slugify(generated_slug)
        return slug

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = self.make_slug()
        super().save(*args, **kwargs)    

    def __str__(self) -> str:
        return self.business_name

class User(AbstractUser):
    
    is_administrator = models.BooleanField(default=False)
    is_moderator = models.BooleanField(default=False)
    business = models.ForeignKey(BusinessId,on_delete=models.CASCADE,null=True)
    phone_number = PhoneField(blank=True,help_text='Contact phone number')
    





