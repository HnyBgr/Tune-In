from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import MusicInfo
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
        this_day = MusicInfo.objects.order_by('name')

        context = {
            # 'message': 'Rock N Roll',
            'this_day': this_day
        }
        return render(request, 'main_app/index.html', context)