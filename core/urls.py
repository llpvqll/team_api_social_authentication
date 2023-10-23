from django.contrib import admin
from django.urls import path, include
from drf_spectacular import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('api/', include('api.urls')),
    path('api/schema/', views.SpectacularAPIView.as_view(), name='schema'),
    path('api/docs', views.SpectacularSwaggerView.as_view(), name='docs'),
]
