from django.urls import path
from .views import  index, mockform

app_name = 'formfill'

urlpatterns = [
    
    path('', index, name='index'),
    path('mockform', mockform, name='mockform'),
    # path('extract_text/', extract_text_from_audio, name='extract_text'),
    # Other URL patterns for your app
]