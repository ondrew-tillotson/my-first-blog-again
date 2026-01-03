from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
#path('admin/', admin.site.urls),
  #  path('', include('blog.urls')),
      path('', views.home_page, name='home_page'), # Only define sub-paths here

    #path('', include('mysite.urls')), # Includes the app's URLs

   # path('', include('mysite.urls')),
    #path('', views.post_list, name='post_list'),
    #path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('upload_csv/', views.upload_csv, name='upload_csv'),
    #path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]

