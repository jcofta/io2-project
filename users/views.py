from django.shortcuts import get_object_or_404,render
from django.http import Http404
from django.http import HttpResponse

from django.contrib.auth import login, authenticate

from users.forms import SignUpForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('../')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
