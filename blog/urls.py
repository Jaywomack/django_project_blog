from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about')
]

for i in range(10):
    i=0
    if i <= 10:
        print(f'The number {i} is less than or equal to 10')
    i= i +1
