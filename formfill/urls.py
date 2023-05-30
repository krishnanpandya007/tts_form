from django.urls import path
from .views import  index

app_name = 'formfill'

urlpatterns = [
    
    path('', index, name='index'),
    # path('extract_text/', extract_text_from_audio, name='extract_text'),
    # Other URL patterns for your app
]