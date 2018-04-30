from django.conf.urls import url
from .views import StudentRudView,StudentCView

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', StudentRudView.as_view(), name="student-rud"),
    url(r'^add/', StudentCView.as_view(), name="student-rud"),
]
