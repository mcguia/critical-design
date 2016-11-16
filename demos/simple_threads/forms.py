from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from simple_threads.models import Employee

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(label = 'Email')
    first_name = forms.CharField(label = 'First Name')
    last_name = forms.CharField(label = 'Last Name')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
'''
    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.first_name = self.cleaned_data["firstname"]
        user.last_name = self.cleaned_data["lastname"]
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()
        return user
        '''

class EmployeeCreateForm(forms.ModelForm):


    rank = forms.IntegerField(label = 'Rank')

    #def __init__(self, *args, **kwargs):
    #    super(EmployeeCreateForm, self).__init__(*args,**kwargs)
        #self.fields.pop('password1')
       # self.fields.pop('password2')


    class Meta:
        model = Employee
        fields = ('rank',)
        exclude = ['user']
'''
    def save(self, commit=True):

        user = super(EmployeeCreateForm, self).save(commit=False)
        user_emp = Employee(rank = self.cleaned_data['rank'])


        if commit:
            user_emp.save()
        return user_emp
        '''