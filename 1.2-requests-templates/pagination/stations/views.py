from django.core.paginator import Paginator
import os
import csv
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # Путь к CSV-файлу
    csv_file_path = settings.BUS_STATION_CSV

    # Чтение данных из CSV-файла
    stations_data = []
    with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            stations_data.append({
                'Name': row['Name'],
                'Street': row['Street'],
                'District': row['District'],
            })

    page_number = request.GET.get('page', 1)

    paginator = Paginator(stations_data, 10)  # Указываем количество объектов на страницу
    page_obj = paginator.get_page(page_number)  # Получаем объекты для текущей страницы

    context = {
        'bus_stations': page_obj,  # Объект страницы с данными
        'page': page_obj,
    }

    return render(request, 'stations/index.html', context)
