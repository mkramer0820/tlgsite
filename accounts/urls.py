from django.conf.urls import url
from django.contrib.auth import login
from accounts.views import logout_view

app_name = 'accounts'

urlpatterns = [

    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout_view, name='logout'),

]
