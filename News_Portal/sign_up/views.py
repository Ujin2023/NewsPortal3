from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import Registration
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

class RegistrationView(CreateView):
    model = User
    form_class = Registration
    success_url = 'posts'
    template_name = 'sign/signup.html'

@login_required
def upgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name='author')
    if not request.user.groups.filter(name='author').exists():
        premium_group.user_set.add(user)
    return redirect('/')
