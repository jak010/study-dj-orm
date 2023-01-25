from django.urls import path

from .views import SampleView

urlpatterns = [
    path('test', SampleView.as_view())
]
