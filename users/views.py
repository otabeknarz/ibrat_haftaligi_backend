from django.shortcuts import render, get_object_or_404
from django.db.models import Count

from .models import User


def stats(request):
    users = User.objects.annotate(invite_count=Count('invitations')) \
        .filter(invite_count__gt=0) \
        .order_by('-invite_count')[:250]
    return render(request, 'stats.html', {'users': users})


def invited_users(request, user_id):
    inviter = get_object_or_404(User, id=user_id)
    invited_users_ = User.objects.filter(invited_by__invited_by=inviter)
    return render(request, 'invited_users.html', {
        'inviter': inviter,
        'invited_users': invited_users_
    })
