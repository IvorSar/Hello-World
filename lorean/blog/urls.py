from django.urls import path 
from blog import views
app_name = 'lorean'

urlpatterns = [
   path("" ,views.base_start , name = 'base_start' ),
   path('video/' , views.video, name = 'video'),
   path('foto/' , views.foto_vision , name = 'foto_vision'),
]

