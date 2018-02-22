"""disc_site URL Configuration

"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('legislator/', include('legislator.urls')),
    path('', RedirectView.as_view(url='/legislator/', permanent=True)),
]

# Keeping if we want to use static files later 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL,\
        document_root=settings.STATIC_ROOT)
