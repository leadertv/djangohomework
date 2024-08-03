from django.shortcuts import render
from django.http import Http404

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def home_view(request):
    return render(request, 'calculator/home.html')


def recipe_view(request, recipe_name):
    recipe = DATA.get(recipe_name)

    # Если рецепт не найден, возвращаем 404
    if recipe is None:
        raise Http404("Рецепт не найден")

    # Получаем параметр servings из GET-запроса
    servings = request.GET.get('servings')

    if servings:
        try:
            servings = int(servings)
            if servings <= 0:
                raise ValueError
        except ValueError:
            servings = 1

    else:
        servings = 1

    adjusted_recipe = {ingredient: amount * servings for ingredient, amount in recipe.items()}

    context = {
        'recipe': adjusted_recipe
    }

    return render(request, 'calculator/index.html', context)
