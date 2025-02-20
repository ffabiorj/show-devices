from django.urls import include, path

from core.views import DeviceView

urlpatterns = [
    path("devices/", DeviceView.as_view(), name="devices"),
]
