from django.urls import path
from .views import tutor_login, tutor_logout, tutor_dashboard, book_slot 

urlpatterns = [
    path('tutor-login/', tutor_login, name='tutor_login'),
    path('tutor-logout/', tutor_logout, name='tutor_logout'),
    path('tutor_dashboard/', tutor_dashboard, name='tutor_dashboard'),
    path('book_slot/', book_slot, name='book_slot'),
]