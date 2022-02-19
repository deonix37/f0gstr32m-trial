from django.urls import path

from . import views

app_name = 'geo_search'
urlpatterns = [
    path('', views.IndexView.as_view()),
    path('ajax/cities', views.AjaxCitiesView.as_view()),
]
