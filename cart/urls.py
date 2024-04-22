from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update-quantity/<int:item>', views.update_quantity, name='update_quantity'),
    path('remove-item/<int:item>', views.remove_item, name='remove_item')
]
