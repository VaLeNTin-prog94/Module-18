from django.shortcuts import render


def class_templates(request):
    return render(request, 'second_task/class_template.html')



