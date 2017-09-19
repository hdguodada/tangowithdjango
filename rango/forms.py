"""
Basic Workflow
1. if you haven't already got one, create a forms.py file within your Django application's directory
2. Create a ModelForm class for each model that you wish to represent as a form.
3. Customise the forms as you desire
4. Create or Update a view to handle the form
- including displaying the form
- saving the form data
- flagging up errors which may occur when the user enters incorrect data(or no data at all) in the form
- create or update a template to display the form
- add a urlpattern to map the new view(if you created a newone)
"""

from django import forms
from rango.models import Page, Category, UserProfile
from django.contrib.auth.models import User



class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text = 'please enter the category name.')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    #An inline class to provide additional information on the form.
    class Meta:
        # provide an association between the ModelForm and model
        model = Category
        fields = ('name', )


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128,
                            help_text="please enter the title of the page.")
    url = forms.URLField(max_length=200,
                         help_text="please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
        'hiding the foreign key'
        exclude = ('category', 'views')
        pass

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url
        return cleaned_data



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
