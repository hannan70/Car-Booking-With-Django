from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('car/', include('cars.urls')),
    path('account/', include('accounts.urls')),
    path("socialaccounts/", include("allauth.urls")),
    path("contact/", include("contacts.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
