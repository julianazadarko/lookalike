# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.template import loader
from django.http import HttpResponse
from django import template
from django import forms
from .models import Profile
from django.contrib import messages

from cloudinary.forms import cl_init_js_callbacks 
from .models import Closet
from .forms import ClosetUploadForm

@login_required(login_url="/login/")
def index(request):
    return render(request, "index.html")

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'error-404.html' )
        return HttpResponse(html_template.render(context, request))

class ClosetUploadView(LoginRequiredMixin, UpdateView):
    model = Closet
    form = ClosetUploadForm
    success_url = reverse_lazy('closet')

    """ def get_object(self):
        return self.user.profile """

    def post(self, request, **kwargs):
        profile_instance = get_object_or_404(Profile, user=request.user)
        update_form = ClosetUploadForm(request.POST, request.FILES, instance=profile_instance)
        if update_form.is_valid():
            update_form.save()
            messages.success(request, f'Your Closet has been updated!')
            return redirect('closet')
        else:
            messages.warning(request, f'Please try again')
            return redirect('closet')


# @login_required
# def closet_upload(request):
#     print("REACHED CLOSET UPLOAD")
#     user = request.user
#     print("REACHED USER GRAB")
#     print(user)
#     #instance = user
#     # instance = get_object_or_404(Profile, user=user)
#     # print("TEST-USER")
#     # if request.method == "POST":
#     #     form = ClosetUploadForm(request.POST, request.FILES, instance=instance)
#     #     print("REACHED CLOSET UPLOAD2")
#     #     if form.is_valid():
#     #         print("REACHED CLOSET UPLOAD3")
#     #         form.save
#     #         return redirect('/')
#     print("REACHED CLOSET UPLOAD4")
#     form = ClosetUploadForm()
#     return render(request, 'closet.html', {'form': form})
