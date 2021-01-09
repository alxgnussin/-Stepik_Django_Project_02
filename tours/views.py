from random import randint

from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render

from .data import departures, tours


def main_view(request):
    random_tours = []
    while len(random_tours) < 6:
        rand = randint(1, len(tours))
        for key, value in tours.items():
            tour = value.copy()
            tour['id'] = key
            if key == rand and tour not in random_tours:
                random_tours.append(tour)

    return render(request, 'index.html',
                  {'departures': departures,
                   'tours': random_tours,
                   })


def departure_view(request, departure):
    depart_tours = []
    for key, value in tours.items():
        if value['departure'] == departure:
            tour = value.copy()
            tour['id'] = key
            depart_tours.append(tour)

    return render(request, 'departure.html',
                  {'departures': departures,
                   'tours': depart_tours,
                   'departure': departures[departure],
                   'word': tour_declension(len(depart_tours)),
                   'min_price': min_max(depart_tours, 'price')[0],
                   'max_price': min_max(depart_tours, 'price')[1],
                   'min_nights': min_max(depart_tours, 'nights')[0],
                   'max_nights': min_max(depart_tours, 'nights')[1],
                   })


def tour_view(request, id):
    tour = tours[id]
    star = int(tour['stars']) * '★'
    depart = departures[tour['departure']]
    return render(request, 'tour.html',
                  {'id': id,
                   'tour': tour,
                   'depart': depart,
                   'departures': departures,
                   'stars': star,
                   })


def tour_declension(num):
    n = int(str(num)[-1])
    m = int(str(num // 10)[-1])
    if n == 1 and m != 1:
        return 'тур'
    elif 1 < n < 5 and m != 1:
        return 'тура'
    else:
        return 'туров'


def min_max(data, key):
    v_list = [item[key] for item in data]
    return min(v_list), max(v_list)


def custom_handler404(request, exception):
    return HttpResponseNotFound('<br/><h1>Ошибка 404</h1><h2>Запрашиваемый ресурс не найден</h2>')


def custom_handler500(request):
    return HttpResponseServerError('<br/><h1>Ошибка 500</h1><h2>Внутренняя ошибка сервера</h2>')
