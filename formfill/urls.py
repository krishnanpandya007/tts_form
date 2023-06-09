from django.urls import path
from .views import  index, mockform, home

app_name = 'formfill'

urlpatterns = [
    
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('mockform/', mockform, name='mockform'),
    
    # path('extract_text/', extract_text_from_audio, name='extract_text'),
    # Other URL patterns for your app
]