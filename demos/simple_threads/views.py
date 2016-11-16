from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from simple_threads import forms
from django.http import HttpResponseRedirect


@login_required
def homepage(request):
    context = {'foo': 'bar'}
    return render(request, 'homepage.html', context)

def contact(request):
    context = {'foo': 'bar'}
    return render(request, 'contact.html', context)

def profile(request):
    context = {'foo': 'bar'}
    return render(request, 'user_profile.html', context)

def register_user(request):
    if request.method == 'POST':
        form1 = forms.UserCreateForm(request.POST)
        form2 = forms.EmployeeCreateForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            user_emp = form2.save(commit=False)
            user_emp.user = user
            user_emp.save()
            return HttpResponseRedirect('/')
        else:
        	messages.error(request, _('Please correct the error below.'))

    else:
	    user_form = forms.UserCreateForm()
	    employee_form = forms.EmployeeCreateForm()

    return render(request, 'registration/register.html', {
        'user_form': user_form,
        'employee_form': employee_form
    })