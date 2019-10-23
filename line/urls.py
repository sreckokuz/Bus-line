from django.urls import path
from . import views

app_name = 'line'

urlpatterns = [
    path('', views.index, name='index_page'),
    path('details/', views.details, name='line_details'),

]
