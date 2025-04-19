from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('books',views.books,name='books'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('api/earnings/', views.earnings_api, name='earnings_api'),


]
