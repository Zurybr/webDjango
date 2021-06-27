from django.contrib import admin
from .models import Article, Category

#configurar el panel adimn
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields=('created_at','update_at')



# Register your models here.
admin.site.register(Article,ArticleAdmin)
admin.site.register(Category)