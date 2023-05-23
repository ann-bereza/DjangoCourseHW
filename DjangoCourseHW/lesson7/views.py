from datetime import datetime

import pytz
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from geopy.geocoders import Nominatim
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from timezonefinder import TimezoneFinder


class PingView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        return Response("PONG")


@csrf_exempt
def get_local_time(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        geolocator = Nominatim(user_agent='time_api')
        location_info = geolocator.geocode(location)
        if location_info:
            time = TimezoneFinder()
            tz = time.timezone_at(lng=location_info.longitude, lat=location_info.latitude)
            cur_timezone = pytz.timezone(tz)
            local_time = datetime.now(cur_timezone)
            return JsonResponse({'location': location, 'local_time': local_time.strftime('%Y-%m-%d %H:%M:%S')})
        else:
            return JsonResponse({'error': 'Invalid location'})

    return JsonResponse({'error': 'Invalid request method'})
