from django.shortcuts import render
from django.views.generic import ListView, DetailView
from.models import Post
# Create your views here.
class PostList(ListView):
    model = Post
    #template_name = 'blog/post_list.html'
    ordering= '-pk'

class PostDetail(DetailView):
    model = Post
    #template_name = 'blog/single_post_page.html'
#def single_post_page(request, pk):
#    post = Post.objects.get(pk=pk)
 #   return render(
 #       request,
 #       'blog/single_post_page.html',
 #       {
 #           'post': post,
 #       }
    