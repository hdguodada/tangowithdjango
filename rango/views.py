from django.shortcuts import render
from .models import Category, Page
from django.views.generic.base import View
from rango.forms import CategoryForm, PageForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from rango.forms import UserProfileForm, LoginForm
from django.contrib.auth import authenticate, login, logout
#Create your views here.

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
        except Category.DoesNotExist:
            contex_dict['pages'] = None
            contex_dict['category'] = None
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



class RegisterView(View):
    def get(self, request):
        profile_form = UserProfileForm()
        return render(request, 'rango/register.html', {
            'profile_form': profile_form,
        })
    def post(self, request):
        registered = False # A boolean value to tell tempalte whether the registion was succesfull,
        profile_form = UserProfileForm(request.POST)
        if profile_form.is_valid():
            # save the user's form data to the database
            profile = profile_form.save(commit=False)
            # hash the password
            profile.set_password(profile.password)
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            # save the user instance
            profile.save()
            # update the variable
            registered = True
            return render(request, 'rango/register.html', {
                'registered': registered,
                'profile_form': profile_form,
            })
        else:
            print(profile_form.errors)
            return render(request, 'rango/register.html', {
                'registered': registered,
                'profile_form': profile_form,
            })


__Add_Login_Functionality__ = """
1. create a login in view to handle user credentials
2. create a login template to display the login form
3. map the login view to a url
4. provide a link to login from the index page
"""
class LoginView(View):
    def get(self, request):
        login_form = LoginForm
        return render(request, 'rango/login.html', {
            'login_form': login_form,
        })

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('rango:index'))
                else:
                    return HttpResponse('Your account is disable')
            else:
                return
