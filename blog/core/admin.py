from django.contrib import admin

from blog.core import models


admin.site.register(models.Article)
admin.site.register(models.Blog)
