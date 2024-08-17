from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    articles = Article.objects.all().order_by('-published_at')  # Упорядочиваем
    context = {
        'object_list': articles  # в контекст
    }

    return render(request, template, context)
