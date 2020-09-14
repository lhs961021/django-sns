from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post, Comment, User
import pdb

def home(request):
    context = {
        'user': request.user,
        'posts': Post.objects.all(),
        'comments': Comment.objects.all(),
    }
    return render(request, 'home.html', context)
