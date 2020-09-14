from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import User, profile
from posts.models import Post
import pdb

# Create your views here.
@login_required
def follow_toggle(request, id):
    user = request.user
    followed_user = get_object_or_404(User, pk=id)
    is_follower = profile in followed_user.profile.followers.all()

    if is_follower:
        profile.followings.remove(followed_user.profile)
        print('팔로우 취소')
    else:
        profile.followings.add(followed_user.profile)
        print('팔로우')

    return redirect('home')

def mypage(request, id):
    mypage_user = get_object_or_404(User, pk=id)
    context = {
        'posts' : Post.objects.filter(user=request.user),
        'followings' : mypage_user.profile.followings.all(),
        'followers' : mypage_user.profile.followers.all(),
    }
    return render(request, 'users/mypage.html', context)