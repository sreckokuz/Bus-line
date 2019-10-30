from django.urls import path
from . import views

app_name = 'line'

urlpatterns = [
    path('', views.index, name='index_page'),
    path('details/', views.details, name='line_details'),
    path('create/<int:id>/', views.create, name='show_and_create'),
    path('details/<int:id>/', views.oneLineDetais, name='one_line_details'),
    path('create/', views.createStation, name='create_line'),
    path('create/save', views.save_stations, name='srkoman'),
    path('delete/<int:id>/', views.delete, name='delete_line'),
    path('update/<int:id>/', views.edit, name='update_line'),
    path('update/<int:id>/save', views.edit_save, name='update_save'),







]
