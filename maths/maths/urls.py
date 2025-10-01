from django.urls import path
from mathapp.views import power_calculator

urlpatterns = [
    path('', power_calculator, name='power_calculator'),
]