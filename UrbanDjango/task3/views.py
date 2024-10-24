from django.shortcuts import render

def platforms_templates(request):
    return render(request, 'third_task/platform.html')


def games_templates(request):
    return render(request, 'third_task/games.html')


def carts_templates(request):
    return render(request, 'third_task/cart.html')
