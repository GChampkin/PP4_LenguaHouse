from django.urls import path
from .views import tutor_login, tutor_logout, tutor_dashboard, book_slot, generate_date_range, create_tutor_slots 

urlpatterns = [
    path('tutor-login/', tutor_login, name='tutor_login'),
    path('tutor-logout/', tutor_logout, name='tutor_logout'),
    path('tutor_dashboard/', tutor_dashboard, name='tutor_dashboard'),
    path('book-slot/', book_slot, name='book_slot'),
    path('generate-date-range/',
         generate_date_range,
         name="generate_date_range"
         ),
    path('create-tutor-slots/', create_tutor_slots, name="create_tutor_slots"),

]
