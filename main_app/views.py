from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import MusicInfo
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.


def index(request, ):
    this_day = MusicInfo.objects.order_by('day')

    year = ""
    artist = ""
    description = ""

    data = {
        # # 'message': 'Rock N Roll',
        'year': year,
        'artist': artist,
        'description': description,
    }
    return render(request, 'main_app/index.html', data)


