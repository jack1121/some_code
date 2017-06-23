from django.conf.urls import url,include
from django.contrib import admin
from  . import views

'''
urlpatterns = [
url(r'^$', views.IndexView.as_view(), name='index'),
url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),]
'''

urlpatterns = [
url(r'^$',views.index,name='index'),
url(r'^login/$',views.login,name='login'),
]