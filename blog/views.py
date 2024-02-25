from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import PostForm
from .models import Post


def home(request):
    context = {"posts": Post.objects.all()}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.author = request.user
            user.save()
            messages.success(request, "The post has been created successfully.")
            return redirect("blog-home")
        else:
            messages.error(request, "Please correct the following errors:")
    else:
        form = PostForm()
    return render(request, "blog/create_post.html", {"form": form})
