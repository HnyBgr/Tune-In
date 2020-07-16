from django.core.management.base import BaseCommand
from main_app.models import MusicInfo
import json
import requests
import time
import random


class Command(BaseCommand):

    def handle(self, *args, **options):
        

        time.sleep(random.randint(1, 10))
        month = ""
        day = ""
        response = requests.get('https://www.thisdayinmusic.com/wp-json/tdim/v1/otd/' + month + '/' + day, headers={'User-Agent': 'Mozilla/5.0'})
        
        data = response.json()

        
        for entry in data:
            day = entry['day']
            month = entry['month']
            year = entry['year']
            artist = entry['artist']
            band = entry['band']
            description = entry['description']
            # print(entry['artist'])

            music_info = MusicInfo(
                day=day,
                month = month,
                year = year,
                artist = artist,
                band = band,
                description = description
            )
            music_info.save()



        # for i, entry in enumerate(data):
        #     print(str(i)+ '-'+str(entry))
       