import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Page, Category


def add_page(category, title, url):
    'get_or_create 返回一个元祖，第一个元素是创建的或者是get到的对象，如果是创建， 第二个元素是True'
    p =  Page.objects.get_or_create(category=category, title=title, url=url)[0]
    return p

def add_category(name):

    c = Category.objects.get_or_create(name=name)[0]
    return c


def populate():
    python_cat = add_category('python')

    add_page(
        category=python_cat,
        title = 'office python',
        url = 'www.baidu.com',
    )

    python_django = add_category('django')

    add_page(
        category=python_django,
        title = 'office django',
        url = 'www.baidu.com',
    )

    # print what we have added in the database
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("{}-{}".format(str(c), str(p)))

if __name__ == '__main__':
    print('begin::::')
    populate()
