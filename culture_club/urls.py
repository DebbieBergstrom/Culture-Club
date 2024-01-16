"""culture_club URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from blog.views import ProfileDeleteView, custom_403_error

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog.urls"), name="blog-urls"),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('allauth.urls')),
    path('account/delete/<int:pk>/', ProfileDeleteView.as_view(), name='account_delete'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Custom error handler for 403
# This assignment tells Django to use the 'custom_403_error' view function to handle HTTP 403 Forbidden errors.
# For other common HTTP errors like 404 (Not Found) and 500 (Internal Server Error), Django automatically uses its default views unless specified otherwise.
# To use custom views for these errors, you can similarly define 'handler404' and 'handler500' here.
handler403 = custom_403_error
