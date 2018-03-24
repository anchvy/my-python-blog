from django.shortcuts import render, get_object_or_404
from django.utils import timezone
# means current directory or current application ( can relative path with ../..)
from .models import Post

# python is dynamic type ( can determine type by type({variable}) )
# def : like a function
# render(request, template_name, context=None, content_type=None, status=None, using=None
def post_list(request):
  # lte : lower than equal
  # filter time < NOW() and ordered by  'published_date'
  posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
  return render(request, 'blog/post_list.html', { 'posts': posts })

def post_detail(request, pk):
  # get_object_or_404(klass, *args, **kwargs)
  post = get_object_or_404(Post, pk=pk)
  return render(request, 'blog/post_detail.html', { 'post': post })
