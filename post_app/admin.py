from post_app.models import Post
from post_app.models import Comment
from django.contrib import admin

#class PostAdmin(admin.ModelAdmin):
        #fields=['user_id', 'title', 'description', 'pub_date', 'publish']

class PostAdmin(admin.ModelAdmin):   
    #fields=('user', 'title', 'description', 'publish')
    fieldsets=(
        ('UserDetails',{'fields':('user','title'),'classes':['collapse']}),
        ('PostDetails',{'fields':(('description','publish')),'classes':['wide']}),
            
       
    )
    

admin.site.register(Post,PostAdmin)
admin.site.register(Comment)


