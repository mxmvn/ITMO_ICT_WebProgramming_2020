from urllib import request

from django.urls import path
from . import views
from .views import ShowAutoView, AutomobilesCreateView

urlpatterns = [
    path('owner/<int:owner_id>', views.detail),
    path('all_owners', views.show_all_owners),
    path('all_cars', ShowAutoView.as_view),
    path('create_automobiles', AutomobilesCreateView.as_view),
]