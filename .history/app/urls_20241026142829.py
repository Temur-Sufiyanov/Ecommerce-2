from django.urls import path
from .views import home, category_view

urlpatterns = [
    path('', home, name='home'),
    path('category/<slug:slug>/', category_view, name='category_view',)
]
