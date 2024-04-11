from django.urls import path
from . import views

app_name = 'index'
urlpatterns = [
   path('', view=views.index, name='index'),
   path('donor/', view=views.donor_view, name='donor'),
   path('receiver/', view=views.receiver_view, name='receiver'),
]