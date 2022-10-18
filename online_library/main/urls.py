from django.contrib import admin
from django.urls import path

from online_library.main.views import show_home, add_book_page, edit_book_page, details_book_page, profile_page, \
    edit_profile_page, delete_profile_page, create_profile

urlpatterns = (
    path('', show_home, name='show home'),

    path('add/', add_book_page, name='add book page'),
    path('edit/<int:pk>/', edit_book_page, name='edit book page'),
    path('details/<int:pk>/', details_book_page, name='details book page'),

    path('profile/', profile_page, name='profile page'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile_page, name='edit profile page'),
    path('profile/delete/', delete_profile_page, name='delete profile page'),
)


""" 
http://localhost:8000/ - home page

http://localhost:8000/add/ - add book page
http://localhost:8000/edit/:id - edit book page
http://localhost:8000/details/:id - book details page

http://localhost:8000/profile/ - profile page
http://localhost:8000/profile/edit/ - edit profile page
http://localhost:8000/profile/delete/ - delete profile page
"""