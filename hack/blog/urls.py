from django.urls import path, include
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.post_list, name="post_list"),
    path('post/<int:pk>/', views.post_detail, name="post_detail"),
    path("post/new/", views.post_new, name="post_new"),
    path("post/<int:pk>/edit/", views.post_edit, name="post_edit"),
    path("register/", views.sign_up, name="sign_up"),
    path("login/", views.log_in, name="log_in"),
    path("logout/", views.log_out, name="log_out"),
    path("tag/<str:tag>", views.tag_info, name="tag-info"),
    path("search", views.post_search, name="search"),
    path("tag-search", views.tag_search, name="tag_search"),
    path("all_tags/", views.all_tags, name="all-tags"),
    path("my_posts/", views.my_posts, name="my_posts"),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]
