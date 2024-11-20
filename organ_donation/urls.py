from django.contrib import admin
from django.urls import include, path
from donors import views as v

urlpatterns = [
    path('donors/', include('donors.urls')),  # Include URLs from donors app
    path('hospitals/', include('hospitals.urls')),  # Include URLs from hospitals app
    path('admin/', admin.site.urls),  # Admin interface URL
    path('home/', v.wedonate, name='wedonate'),  # Home URL pattern
    # Add a pattern for the root URL
    path('', v.wedonate, name='home'),  # Maps the root URL to the 'wedonate' view
]
