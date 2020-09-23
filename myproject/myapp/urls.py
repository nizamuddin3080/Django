from django.urls import path
from . import views
from myapp.views import AboutView       #about urls


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', AboutView.as_view()), #About Temlates 
]
