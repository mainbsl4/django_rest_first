from django.urls import path
from myapp import views

urlpatterns = [
    path('contact/', views.DataList.as_view()),
    path('contact/<int:pk>/', views.DataDetail.as_view()),
]