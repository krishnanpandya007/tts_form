from django.urls import path
from .views import extract_text_from_audio, home

app_name = 'formfill'

urlpatterns = [
    
    path('home/', home, name='home'),
    path('extract_text/', extract_text_from_audio, name='extract_text'),
    # Other URL patterns for your app
]