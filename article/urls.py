from django.urls import path
from django.contrib import admin
from . import views


app_name = "article"

urlpatterns = [
    path('frontend_test/', views.frontend_test, name="frontend_test"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('add_article/', views.add_article, name="add_article"),
    path('article/<int:id>/', views.detail, name="detail"),
    path('update/<int:id>/', views.update_article, name="update"),
    path('delete/<int:id>/', views.delete_article, name="delete"),
    path('',views.articles, name="articles"),
    path('comment/<int:id>', views.add_comment, name="comment")
]