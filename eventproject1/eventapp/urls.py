from django.urls import path
from . import views

urlpatterns = [
    path('eventapp/', views.ListEventView.as_view(), name='list-event'),
    path('eventapp/<int:pk>/detail/', views.DetailEventView.as_view(), name='detail-event'),
    path('eventapp/create/', views.CreateEventView.as_view(), name='create-event'),
    path('eventapp/<int:pk>/delete/', views.DeleteEventView.as_view(), name='delete-event'),
    path('eventapp/<int:pk>/update/', views.UpdateBookView.as_view(), name='update-event'),
]