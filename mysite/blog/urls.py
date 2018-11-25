from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('allposts', views.all_posts, name='all_posts'),
    path('post/<int:post_num>', views.single_post, name='single_post'),
    path('book/<str:book_title>', views.posts_by_book, name='posts_by_book'),
]