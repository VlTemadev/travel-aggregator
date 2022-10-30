from django.contrib import admin
from . import views
from django.urls import path
from .views import CategoryListView, PostByCategoryView, AboutListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CategoryListView.as_view(), name='category-list'),
    path('<str:slug>/', PostByCategoryView.as_view(), name='post-by-category'),
    path('post/<int:pk>/', views.postDetail, name='postDetail'),
]

