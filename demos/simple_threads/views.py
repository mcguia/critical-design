from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from simple_threads import forms
from django.http import HttpResponseRedirect
from django_comments_xtd import (get_form, comment_was_posted, signals, signed,
                                 get_model as get_comment_model)

from django_comments_xtd.models import (TmpXtdComment,
                                        max_thread_level_for_content_type,
                                        LIKEDIT_FLAG, DISLIKEDIT_FLAG)

from simple_threads.models import Employee


@login_required
def homepage(request):
    context = {'foo': 'bar'}
    return render(request, 'homepage.html', context)

@login_required
def contact(request):
    context = {'foo': 'bar'}
    return render(request, 'contact.html', context)

@login_required
def profile(request):
    context = {'foo': 'bar'}
    return render(request, 'user_profile.html', context)

def user_comments(request):
	curr_user = request.user
	XtdComment = get_comment_model()
	comments = XtdComment.objects.filter(user_id=curr_user.id)
	context = {'comments': comments}
	return render(request, 'user_comments.html', context)


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