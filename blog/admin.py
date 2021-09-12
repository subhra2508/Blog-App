from django.contrib import admin
from django.db.models.query import prefetch_related_objects

from blog.models import Post




# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','publish','status')

    #The list page now includes a right sidebar that allows you to filter the results by
    #the fields include in the list_filter
    list_filter = ('status','created','publish','author')

    search_fields = ('title','body')

    #you are telling django to prepopulate the slug field using title
    prepopulated_fields = {'slug':('title',)}

    #the author field is now displayed with a lookup widget that can scale much better than a drop-down
    #select input when you have thousands of users for this we are using the raw_id_fields
    raw_id_fields = ('author',)

    #below the search bar there are navigation links to navigate through date hierarchy
    date_hierarchy = 'publish'

    #we can see that the posts are ordered by status and publish columns by default as we define
    #the default sorting criteria using ordering attribute
    ordering = ('status','publish')

