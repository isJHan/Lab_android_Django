# from YikE.comments.views import comment
from django.contrib import admin
from .models import comment as commentTable
# Register your models here.
admin.site.register(commentTable)