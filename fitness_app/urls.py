from django.contrib import admin
from django.urls import include, path
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name='home'),  # Home Page
    path("users/", include('users.urls')),  # Users App URLs
    path("accounts/", include("allauth.urls")),  # Include Allauth URLs for social logins (fix)
    path('__debug__/', include('debug_toolbar.urls')),
]