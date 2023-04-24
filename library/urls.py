"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.book_login),
    path('welcome/', views.home, name="home_page"),
    path('show-book/', views.show_book, name="show_book"),
    path('update/<int:pk>/', views.update_book, name="update_book"),
    path('delete/<int:pk>/', views.delete_book, name="delete_book"),
    # path('books/', views.show_book, name="all_active_books"),
    path('soft-delete/<int:pk>/', views.soft_delete_book, name="soft_delete_book"),
    path('inactive-books/', views.show_inactive_books, name="all_inactive_books"),
    path('restore-books/<int:pk>/', views.restore_book, name="restore_book"),



    path("book-form/", views.book_form, name="book_form"),
    path("book-login/", views.book_login, name="book_login"),
    path("book-logout/", views.book_logout, name="book_logout"),




    
]
