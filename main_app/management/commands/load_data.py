from django.core.management.base import BaseCommand
from main_app.models import MusicInfo
import json
import requests
import time
import random


class Command(BaseCommand):

    def handle(self, *args, **options):
        

        time.sleep(random.randint(1, 10))

        response = requests.get('https://www.thisdayinmusic.com/wp-json/tdim/v1/otd/7/1/', headers={'User-Agent': 'Mozilla/5.0'})
        
        data = response.json()
        
        for entry in data:
            day = entry['day']:
            month = entry['month']:
            year = entry['year']:
            artist = entry['artist']
            description = entry['description']:
            # print(entry['artist'])

       