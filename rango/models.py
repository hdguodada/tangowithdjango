from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProfile(AbstractUser):
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, null=True, blank=True)


    def save(self, *args, **kwargs):
        'category.name will have some whitespace inside, we could import slugify change whitespace to -'
        self.slug= slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'categorie'
        verbose_name_plural = verbose_name


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
