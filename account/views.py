from django.contrib import auth, messages
from django.contrib.auth import login, authenticate, logout
from .forms import SignupForm
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# 회원가입

def home(request):
	return render(request, 'erp/main.html')
def signup(request):
	if request.method == 'POST':
		if request.POST['password'] == request.POST['password2']:
			user = User.objects.create_user(
				username=request.POST['username'],
				password=request.POST['password'],
				email=request.POST['email'],
			)
			auth.login(request, user)
			return redirect('/')
		return render(request, 'account/signup.html')
	else:
		user = request.user.is_authenticated
		if user:
			return redirect('/')
		else:
			CreateForm = SignupForm()
			return render(request, 'account/signup.html', {'form':CreateForm})


def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		print(user)
		if user is not None:
			login(request, user)
			return redirect('/')
		else:
			messages.error(request, '아이디와 패스워드가 다릅니다.')
		return render(request, 'account/login.html')
	elif request.method == 'GET':
		user = request.user.is_authenticated
		if user:
			return redirect('/')
		else:
			return render(request, 'account/login.html')

@login_required
def logout_view(request):
	auth.logout(request)
	return redirect('/')