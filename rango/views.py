from django.shortcuts import render
from .models import Category, Page
from django.views.generic.base import View
from rango.forms import CategoryForm, PageForm
from django.http import HttpResponseRedirect
from django.urls import reverse
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



class Add_category(View):
    form = CategoryForm()
    def get(self, request):
        return render(request, 'rango/add_category.html', {
            'form': self.form,
        })


    def post(self, request):
        form = CategoryForm(request.POST)
        # provide a valid form?
        if form.is_valid():
            # Save the new category to the database
            form.save(commit=True)
            # Now the category is saved.
            # we could give a confirmation message
            # but since the most recent category added is on the page.
            # Then we can direct the user back to the index page.
            return HttpResponseRedirect(reverse('rango:index'))
        else:
            # the supplied form contained errors
            # just print them to the terminal
            print(form.errors)
            return render(request, 'rango/add_category.html', {
                'form': form,
            })


class Add_Page(View):
    def get(self, request, category_name_slug):
        form = PageForm()
        category = Category.objects.get(slug=category_name_slug)
        return render(request, 'rango/add_page.html', {
            'form': form,
            'category': category,
        })

    def post(self, request, category_name_slug):
        try:
            cat = Category.objects.get(slug=category_name_slug)
            pass
        except Category.DoesNotExist:
            cat = None
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                page.views = 0
                page.save()
                return HttpResponseRedirect(reverse('rango:category', args=(cat.slug,)))
            else:
                print('111')
                return render(request, 'rango/add_page.html', {
                    'form': form,
                })
