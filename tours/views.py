from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render


def main_view(request):
    return render(request, 'tours/index.html')


def departure_view(request, departure):
    return render(request, 'tours/departure.html', departure=departure)


def tour_view(request, id):
    return render(request, 'tours/tour.html', id=id)


def custom_handler404(request, exception):
    return HttpResponseNotFound('<br/><h1>Ошибка 404</h1><h2>Запрашиваемый ресурс не найден</h2>')


def custom_handler500(request):
    return HttpResponseServerError('<br/><h1>Ошибка 500</h1><h2>Внутренняя ошибка сервера</h2>')
