from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',

                       # url(r'^add/$', views.add_archive, name='add_archive'),
                       url(r'^upload/$', views.upload, name='upload_docs'),
                       url(r'^contact/$', views.contact, name='contactus'),

    url(r'^$', views.index, name="feel_home"),
    url(r'^templates/(?P<template_name>\w+)', views.angularTemplate, name="angularTemplate"),

    url(r'^api/books/$', views.apiGallery, name="apiGallery"),
    url(r'^api/books/(?P<archive_id>\d+)/$', views.apiGallery, name="apiGallery"),
    # url(r'^api/photos/(?P<photos>\w+)/table/(?P<table>\w+)', views.apiTable, name='apiTable'),


)
