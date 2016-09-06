from django.shortcuts import render, redirect
from django.template import RequestContext
from blog.form import PostForm
from .models import Post



def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            te = form.save()

            return redirect('../../',permanent=True)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


