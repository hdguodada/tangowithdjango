from django.shortcuts import render
from .models import Category, Page
from django.views.generic.base import View
# Create your views here.

class IndexView(View):
    # Query database for a list of all categoryies currently stored
    # order the categoryies by 'likes'
    # place the list in our context_dict will passed to the template engine
    def get(self, request):
        category_list = Category.objects.order_by('-likes')[0:5]
        context_dict = {
            'category_list': category_list,
        }
        return render(request, 'rango/index.html', context_dict)


class AboutView(View):
    def get(self, request):
        return render(request, 'rango/about.html', {
            'my_name': '郭靖',
        })


class DetailView(View):
    def get(self, request, category_name_slug):
        # create a context dict to pass the template egine
        contex_dict = {}
        try:
            category = Category.objects.get(slug=category_name_slug)
            pages = Page.objects.filter(category=category)
            contex_dict['pages'] = pages
            contex_dict['category'] = category
            pass
        except Category.DoesNotExist:
            contex_dict['pages'] = None
            contex_dict['category'] = None
            pass
        return render(request, 'rango/category.html', contex_dict)
