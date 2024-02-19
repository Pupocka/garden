from django.urls import path

from cotalog import views

app_name = 'cotalog'

urlpatterns = [
    path('', views.PlantsView.as_view())
]