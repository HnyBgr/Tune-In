from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import MusicInfo
from django.urls import reverse
from django.http import HttpResponseRedirect

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

def sign_up(request):
    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        verify_password = request.POST['verify_password']

        if password != verify_password:
            return HttpResponse('Passwords do not match!')

        user = User.objects.create_user(username, email, password)
        return HttpResponseRedirect(reverse('main_app/index.html'))
    
    return render(request, 'main_app/sign_up.html' )

def motion(request):
    return render(request, 'main_app/motion.html')



