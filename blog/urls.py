from django.urls import path
from . import views
#test
urlpatterns = [
	path('', views.post_list, name='post_list'),
	path('about', views.about, name='about'),
	path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
	path('drafts/', views.post_draft_list, name='post_draft_list'),
	path('post/<pk>/publish/', views.post_publish, name='post_publish'),
	path('post/<pk>/remove/', views.post_remove, name='post_remove'),
	path('post/<pk>/edit/', views.post_edit, name='post_edit'),
]
