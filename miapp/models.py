from django.db import models

# Create your models here.
#makemigration
#python manage.py sqlmigrate miapp 0001
#migrate

class Article(models.Model):
    title=models.CharField(max_length=101) #se puede usar el verbose_name= tambien
    content=models.TextField()
    image=models.ImageField(default='null',upload_to='articles')
    published=models.BooleanField()
    created_at=models.DateField(auto_now_add=True)
    update_at=models.DateField(auto_now=True)

    class Meta:
        '''db_table="nombretabla"'''
        verbose_name="Articulo"
        verbose_name_plural="Articulos"
        ordering=['-id']

    def __str__(self):
        if self.published:
            publicado='publicado'
        else:
            publicado='no publicado'
        return f"**|{self.id}|** con titulo **|{self.title}|** {publicado} "



class Category(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=255)
    create_at=models.DateField()
