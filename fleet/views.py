from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Fleet, Order
from googlemaps import Client as GoogleMaps
import json

gmaps = GoogleMaps(key='YOUR_GOOGLE_MAPS_API_KEY')

@csrf_exempt
def create_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        order = Order.objects.create(**data)
        return JsonResponse({'success': True, 'order_id': order.id})

def calculate_distance(pickup, unload, load, drop_off):
    addresses = [pickup, unload, load, drop_off]
    points = [a for a in addresses if a]
    if len(points) < 2:
        return 0
    distance = 0
    for i in range(len(points) - 1):
        directions = gmaps.directions(points[i], points[i + 1])
        distance += directions[0]['legs'][0]['distance']['value']
    return distance / 1000