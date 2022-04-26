from django.urls import path
from .views import home,addMusic


urlpatterns = [
    path('', home, name='home'),
    path('add/',addMusic, name='add_music' ),
    # path('', )
]
