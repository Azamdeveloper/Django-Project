from django.urls import path
from news.views import home_page, about_detail
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", home_page, name="home"),
    path('about_detail/<int:pk>/', about_detail, name="about_detail")
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


