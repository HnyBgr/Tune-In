from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
        this_day = MusicInfo.objects.order_by('name')
        context = {
            'message': 'Rock N Roll',
            'this_day': this_day
        }
        return render(request, 'main_app/index.html', context)