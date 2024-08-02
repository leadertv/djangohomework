from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse
import os
from datetime import datetime


def format_current_time():
    """Форматирует текущее время в строку."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def home_view(request):
    """Главная страница с ссылками на другие разделы."""
    template_name = 'app/home.html'

    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('current_time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
    }

    context = {'pages': pages}
    return render(request, template_name, context)


def time_view(request):
    """Возвращает текущее время."""
    current_time = format_current_time()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    """Возвращает список файлов в рабочей директории в текстовом формате."""
    try:
        workdir = os.getcwd()
        files = os.listdir(workdir)
        file_list = [f for f in files]
        return HttpResponse('\n'.join(file_list))  # В строку
    except Exception as e:
        return HttpResponse(f'Ошибка: {str(e)}', status=500)