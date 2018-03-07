"""disc_site URL Configuration

"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from legislator import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('legislator/', include('legislator.urls')),
    path('home/', views.home, name="home"),
    path('non_disc/', views.non_disc, name="non_disc"),
    path('full_results/', views.full_results, name="full_results"),
    path('', RedirectView.as_view(url='/home/')),
]

# Keeping if we want to use static files later
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL,\
        document_root=settings.STATIC_ROOT)
