from django.shortcuts import render


def platforms_templates(request):
    return render(request, 'fourth_task/platform.html')


def games_templates(request):
    data = {'games': ["Atomic Heart", "Cyberpunk 2077", "PayDay"]}
    return render(request, 'fourth_task/games.html', context=data)


def carts_templates(request):
    return render(request, 'fourth_task/cart.html')
