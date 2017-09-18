import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Page, Category


def add_page(category, title, url):
    'get_or_create 返回一个元祖，第一个元素是创建的或者是get到的对象，如果是创建， 第二个元素是True'
    p =  Page.objects.get_or_create(category=category, title=title, url=url)[0]
    return p

def add_category(name, views=0, likes=0):

    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c


def populate():
    python_cat = add_category('Python', views=127, likes=64)

    add_page(category=python_cat,
        title="Official Python Tutorial",
        url="http://docs.python.org/2/tutorial/")

    add_page(category=python_cat,
        title="How to Think like a Computer Scientist",
        url="http://www.greenteapress.com/thinkpython/")

    add_page(category=python_cat,
        title="Learn Python in 10 Minutes",
        url="http://www.korokithakis.net/tutorials/python/")

    django_cat = add_category("Django", views=64, likes=32)

    add_page(category=django_cat,
        title="Official Django Tutorial",
        url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")

    add_page(category=django_cat,
        title="Django Rocks",
        url="http://www.djangorocks.com/")

    add_page(category=django_cat,
        title="How to Tango with Django",
        url="http://www.tangowithdjango.com/")

    frame_cat = add_category("Other Frameworks", views=32, likes=16)

    add_page(category=frame_cat,
        title="Bottle",
        url="http://bottlepy.org/docs/dev/")

    add_page(category=frame_cat,
        title="Flask",
        url="http://flask.pocoo.org")
    # print what we have added in the database

if __name__ == '__main__':
    print('begin::::')
    populate()
