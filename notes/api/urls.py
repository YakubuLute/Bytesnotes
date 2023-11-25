from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('notes/', views.getNotes, name="notes"),
    path('note/create/', views.createNote, name="create_note"),
    path('note/<str:pk>/', views.getNote, name="note"),
    path('note/<str:pk>/delete/', views.deleteNote, name="delete"),
    path('note/<str:pk>/update/', views.updateNote, name="update-note"),
]
