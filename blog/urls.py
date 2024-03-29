from django.urls import path
from django.urls.resolvers import URLPattern


# from blog.views import post_list
from blog.views import post_detail,PostListView

app_name = 'blog'

urlpatterns = [
    # path('',post_list,name='post_list'),
    path('',PostListView.as_view(),name="post_list"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',post_detail,name='post_detail')
]