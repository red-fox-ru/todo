from django.urls import path

from todos import views

urlpatterns = [
    path('todo/', views.todo_list, name='todo'),
    path('todo/<int:pk>', views.todo_detail),
]
