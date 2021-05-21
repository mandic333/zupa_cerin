from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('glasnici/', views.GlasniciListView.as_view(), name='glasnici'),
    path('vijesti/', views.VijestiView.as_view(), name='vijesti'),
    path('vijesti/<slug>', views.VijestiDetailView.as_view(), name='vijesti_detail'),
    path('povijest/', views.PovijestView.as_view(), name='povijest'),
    path('kontakt/', views.KontaktFormView.as_view(), name='kontakt'),
    re_path('djga/', include('google_analytics.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

