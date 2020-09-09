from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import User


# Create your views here.
@login_required
def follow_toggle(request, id):
    user = request.user
    profile = user.profile

    followed_user = get_object_or_404(User, pk=id)

    is_follower = profile in followed_user.profile.followers.all()

    if is_follower:
        profile.followings.remove(followed_user.profile)
        print('팔로우 취소')
    else:
        profile.followings.add(followed_user.profile)
        print('팔로우')

    return redirect('home')