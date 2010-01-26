#!/usr/bin/env python
from django.conf.urls.defaults import *
from django.views.generic import list_detail
from estate.models import Estate

estate_info = {
    "queryset" : Estate.objects.all(),
}

urlpatterns = patterns('',
    (r'^list/', list_detail.object_list, estate_info)
)

