from django.urls import re_path
from .views import EmployeeList, EmployeeDetail

urlpatterns = [
    re_path(r'^$', EmployeeList.as_view()),
    re_path(r'^(?P<pk>[0-9]+)/$', EmployeeDetail.as_view()),
]
