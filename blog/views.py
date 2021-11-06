from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView


from blog.models import Post


# before pagination 
# def post_list(request):
#     posts = Post.published.all()
#     context = {'posts':posts}
#     return render(request,'blog/post/list.html',context)

#using pagination through function based view

# def post_list(request):
#     object_list = Post.published.all();
#     paginator = Paginator(object_list, 3)
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         #if page not an integer deliver the first page
#         posts = paginator.page(1)
#     except EmptyPage:
#         # if page is out of range deliver last page of results
#         posts = paginator.page(paginator.num_pages)
#     context = {
#         'page':page,
#         'posts':posts
#     }
#     return render(request,'blog/post/list.html',context)


## using pagination through class based views
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'



def post_detail(request,year,month,day,post):
    post = get_object_or_404(
        Post,
        slug=post,
        status='published',
        publish__year = year,
        publish__month = month,
        publish__day = day
        )
    return render(request,'blog/post/detail.html',{'post':post})