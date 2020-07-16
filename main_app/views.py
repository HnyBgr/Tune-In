from django.shortcuts import render, reverse, get_object_or_404, reverse
from django.http import HttpResponse
from .models import MusicInfo
# from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    this_day = MusicInfo.objects.order_by('day')

    year = ''
    artist = ''
    description = ''

    data = {
        # # 'message': 'Rock N Roll',
        'year': year,
        'artist': artist,
        'description': description,
    }
    return render(request, 'main_app/index.html', data)

# view for login user
def login_user(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['psw']

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is None:
            return render(request, 'main_app/login_user.html', {'message': 'No user with that username and password'})
        
        login(request, user)
        return HttpResponseRedirect(reverse('main_app:index'))
    return render(request, 'main_app/login_user.html')

# view for logout user
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('main_app:index'))

# view for sign up user
def sign_up(request):
    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['psw']
        verify_password = request.POST['psw-verify']

        if password != verify_password:
            return HttpResponse('Passwords do not match!')

        user = User.objects.create_user(username, email, password)
        return HttpResponseRedirect(reverse('main_app:index'))
    
    return render(request, 'main_app/sign_up.html')
    
# view to test animation
def motion(request):
    return render(request, 'main_app/motion.html')



