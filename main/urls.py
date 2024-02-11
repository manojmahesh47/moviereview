from django.urls import path
from . import views
app_name = "main"
urlpatterns = [
    path('',views.home,name="home"),
    path('details/<int:id>/',views.detail,name="details"),
    path('add_movies/', views.add_movies, name='add_movies'),
    path('edit_movies/<int:id>/', views.edit_movies, name='edit_movies'),
    path('delete_movies/<int:id>/', views.delete_movies, name='delete_movies'),
    path('addreview/<int:id>/',views.add_review,name="add_review"),
    path('editreview/<int:movie_id>/<int:review_id>/',views.edit_review,name="edit_review"),
]
