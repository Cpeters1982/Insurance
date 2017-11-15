from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from mysite.core import views as core_views
"""
from mysite.upload import views as upload_views
maybe? and then...
url(r'^upload/$', upload_views.upload, name='upload'),
"""


urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    
]
