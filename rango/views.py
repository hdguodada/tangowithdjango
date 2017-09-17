from django.shortcuts import render

# Create your views here.


def hello(request):
    context_dict = {
        'boldmessage': "guojing",
    }
    return render(request, 'rango/index.html', context_dict)


def about(request):
    return render(request, 'rango/about.html', {
        'my_name': '郭靖',
    })
