from django.urls import path
from .views import posts_list,posts_details,add_post
urlpatterns = [
    path('', posts_list),
    path('details/<id>/', posts_details),
    path('add/', add_post),
]
