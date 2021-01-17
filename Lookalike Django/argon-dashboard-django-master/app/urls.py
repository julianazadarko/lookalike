# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from django.conf.urls import url
from app import views

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    re_path(r'^.*\.html', views.pages, name='pages'),

    # The home page
    path('', views.index, name='home'),
    path('closet/', views.ClosetUploadView.as_view(template_name='core/closet.html'), name='closet'),
    #url(r'^upload$', views.closet_upload, name='views.closet_upload'),
]
