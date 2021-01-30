import random

from django.http import HttpResponseNotFound, HttpResponseServerError, Http404
from django.shortcuts import render

from .data import departures, tours


def main_view(request):
    random_tours = []
    while len(random_tours) < 6:
        rand = random.randint(1, len(tours))
        for tour_id, tour in tours.items():
            tour = tour.copy()
            tour['id'] = tour_id
            if tour_id == rand and tour not in random_tours:
                random_tours.append(tour)

    return render(request, 'index.html', {
        'departures': departures,
        'tours': random_tours,
    })


def departure_view(request, departure):
    depart_tours = []
    for tour_id, tour in tours.items():
        if tour['departure'] == departure:
            tour = tour.copy()
            tour['id'] = tour_id
            depart_tours.append(tour)

    return render(request, 'departure.html', {
        'departures': departures,
        'tours': depart_tours,
        'departure': departures[departure],
        'min_price': min(tour['price'] for tour in depart_tours),
        'max_price': max(tour['price'] for tour in depart_tours),
        'min_nights': min(tour['nights'] for tour in depart_tours),
        'max_nights': max(tour['nights'] for tour in depart_tours),
    })


def tour_view(request, id):
    try:
        tour = tours[id]
    except:
        raise Http404()
    depart = departures[tour['departure']]
    return render(request, 'tour.html', {
        'id': id,
        'tour': tour,
        'depart': depart,
        'departures': departures,
    })


def custom_handler404(request, exception):
    return HttpResponseNotFound('<br/><h1>Ошибка 404</h1><h2>Запрашиваемый ресурс не найден</h2>')


def custom_handler500(request):
    return HttpResponseServerError('<br/><h1>Ошибка 500</h1><h2>Внутренняя ошибка сервера</h2>')
