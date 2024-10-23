from django.shortcuts import render


def class_templates(request):
    return render(request, 'second_task/class_template.html')


def func_templates(request):
    return render(request, 'second_task/func_template.html')
