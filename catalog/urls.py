from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogsListView.as_view(), name='blogs'),
    path('bloggers/<int:pk>', views.BlogsListbyBloggersView.as_view(), name='blogs_list_by_bloggers'),
    path('blogs/<int:pk>', views.BlogsDetailView.as_view(), name='blogs-detail'),
    path('bloggers/', views.BloggersListView.as_view(), name='bloggers'),
    path('blogs/<int:pk>/comment/', views.CommentCreate.as_view(), name='comment'),

]
