from .models import Post
from profiles.models import Profile
from django.http import HttpResponse
from django.shortcuts import redirect

def action_permission(func):
    def wrapper(request, **kwargs):
        pk = kwargs.get("pk")
        post = Post.objects.get(pk=pk)
        profile = Profile.objects.get(user=request.user)

        if profile.user == post.author.user:
            return func(request, **kwargs)
        else:
            return redirect("posts:main-board")

    return wrapper