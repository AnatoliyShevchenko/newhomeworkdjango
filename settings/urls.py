from django.contrib import admin
from django.urls import path

from apps.main.views import ButtonView, KeyboardView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('button/', ButtonView.as_view()),
    path('keyboard/', KeyboardView.as_view()),

] 
