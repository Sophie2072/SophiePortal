from django.contrib import admin

# Register your models here.
from clio import models


# 把models里的表连接到admin，可以在admin里编辑
admin.site.register(models.Staff)
admin.site.register(models.Member)
admin.site.register(models.Card)