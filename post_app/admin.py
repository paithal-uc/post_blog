from post_app.models import Post
from post_app.models import Comment
from django.contrib import admin

#class PostAdmin(admin.ModelAdmin):
        #fields=['user_id', 'title', 'description', 'pub_date', 'publish']

admin.site.register(Post)
admin.site.register(Comment)