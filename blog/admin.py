from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display=('title','slug','status')
    search_field=['title']
    last_filter=('status',)
    prepopulate_fields={'slug':('title',)}
    summernote_fields=('content',)


# Register your models here.
admin.site.register(Comment)