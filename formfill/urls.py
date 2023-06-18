from django.urls import path
from .views import  index, home2, mockform, home

app_name = 'formfill'

urlpatterns = [
    
    # path('', index, name='index'),
    # path('home2/', home2, name='home2'),
    path('', home, name='home'),
    path('mockform/', mockform, name='mockform'),
    
    # path('extract_text/', extract_text_from_audio, name='extract_text'),
    # Other URL patterns for your app
]