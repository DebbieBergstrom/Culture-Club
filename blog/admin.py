from django.contrib import admin
from .models import Blogpost
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Blogpost)
class PostAdmin(SummernoteModelAdmin):
    
    summernote_fields = ('content')
