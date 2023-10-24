from django.urls import path
from . import views

urlpatterns = [
    path('product', views.get_all_create),
    path('product/<int:id>', views.get_one_edit_delete),
    path('order', views.order)
]
