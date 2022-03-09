
from email.mime import image
import imp
from xml.parsers.expat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.utils.translation import gettext as _

from django.forms import UUIDField
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.


AGE_CHOICES = (
    ('All', 'All'),
    ('Kids', 'Kids')
)


MOVIE_CHOICES = ( 
    ('seasonal' , 'Seasonal'),
    ('single' , 'Single'),
)
class Customer(AbstractUser):
    profiles = models.ManyToManyField("Profile",  verbose_name=_("profile") , blank=True, null=True)

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def __str__(self):
        return str(self.profile)

class Profile(models.Model):
    name = models.CharField(_("name"), max_length=50)
    age_limit = models.CharField(_("age limit"), choices=AGE_CHOICES, max_length=50)
    uuid = models.UUIDField(_("uuid") , default=uuid.uuid4)

    

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(_("title"), max_length=50)
    description = models.TextField(_("description"))
    created = models.DateTimeField(_("created"),  auto_now_add=True)
    uuid = models.UUIDField(_("uuid") , default=uuid.uuid4)
    type = models.CharField(_("age limit"), choices=MOVIE_CHOICES, max_length=50)
    video = models.ManyToManyField("Video", verbose_name=_("video"))
    image = models.ImageField(_("image"), upload_to='cover/', blank=True, null=True)
    age_limit = models.CharField(_("age limit"), choices=AGE_CHOICES, max_length=50)
    slug = models.SlugField(_("slug") , blank=True, null=True)
   
    

    class Meta:
        verbose_name = _("Movie")
        verbose_name_plural = _("Movies")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("netflix:MovieDetail", kwargs={"slug": self.slug})
   

class Video(models.Model):
    title = models.CharField(_("title"), max_length=1500)
    file = models.FileField(_("file"), upload_to='movies/', max_length=100)

    

    class Meta:
        verbose_name = _("Video")
        verbose_name_plural = _("Videos")

    def __str__(self):
        return self.title



