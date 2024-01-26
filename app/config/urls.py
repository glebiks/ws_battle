from django.contrib import admin
from django.urls import path
from api.views import TokenObtainView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", TokenObtainView.as_view()),
]
