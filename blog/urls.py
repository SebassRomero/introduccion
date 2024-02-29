from django.urls import path
from .views import BloglistView, BlogCreateView,BlogdDetailView,BlogUpdateView,BlogDelete
app_name='blog'

urlpatterns = [
  
  path('',BloglistView.as_view(),name='home'),
  path('create/',BlogCreateView.as_view(),name='create'),
  path('<int:pk>/',BlogdDetailView.as_view(),name='detail'),
  path('<int:pk>/update/',BlogUpdateView.as_view(),name='update'),
  path('<int:pk>/delete/',BlogDelete.as_view(),name='delete')
]