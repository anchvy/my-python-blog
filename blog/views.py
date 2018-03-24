from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import PostForm
# means current directory or current application ( can relative path with ../..)
from .models import Post

# python is dynamic type ( can determine type by type({variable}) )
# def : like a function
# render(request, template_name, context=None, content_type=None, status=None, using=None
def post_list(request):
  # lte : lower than equal
  # ordered by  primary key
  posts = Post.objects.order_by('-pk')
  return render(request, 'blog/post_list.html', {'posts': posts })

def post_detail(request, pk):
  # get_object_or_404(klass, *args, **kwargs)
  post = get_object_or_404(Post, pk=pk)
  return render(request, 'blog/post_detail.html', {'post': post })

def post_new(request):
  if (request.method == 'POST'):
    form = PostForm(request.POST)

    if (form.is_valid()):
      # creates and saves a database object from the data bound to the form.
      # commit is true by default, but if false, that means that we don't want to save the Post model yet
      post = form.save(commit=False)
      # add author / published_date before final save
      post.author = request.user
      post.published_date = timezone.now()
      # final save
      form.save()

      # redirect when completely save
      return redirect('post_detail', pk=post.pk)
  else:
    form = PostForm()

  return render(request, 'blog/post_composer.html', {'form': form })

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if (request.method == 'POST'):
        # pass this post as an instance
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        print(form.initial)

    return render(request, 'blog/post_composer.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk).delete()
    return redirect('post_list')

    

