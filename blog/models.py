from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#objects = models.Manager() #The default manager.
#published = PublishedManager() #our custom manager

#custom manager
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICE = (
        ('draft','Draft'),
        ('published','Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICE,default='draft')

    objects = models.Manager() #the default manager
    published = PublishedManager() #our custom manager

    #the meta class inside the model contains meta data.Basically we are telling 
    #django to sort results by the publish field in descending order by default when you query
    #the data base.we are specifying the descending order using the negative prefix.By doing this,
    #post publishing recently will appear first
    class Meta:
        ordering = ('-publish',)

    #you will use the get_absolute_url() method in your templates to link to specific posts
    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.slug
        ])
    
    def __str__(self):
        return self.title
 
