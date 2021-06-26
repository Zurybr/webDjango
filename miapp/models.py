from django.db import models

# Create your models here.
#makemigration
#python manage.py sqlmigrate miapp 0001
#migrate

class Article(models.Model):
    title=models.CharField(max_length=101)
    content=models.TextField()
    image=models.ImageField(default='null')
    published=models.BooleanField()
    created_at=models.DateField(auto_now_add=True)
    update_at=models.DateField(auto_now=True)


class Category(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=255)
    create_at=models.DateField()
