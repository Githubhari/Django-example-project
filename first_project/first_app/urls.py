from django.contrib import admin
from django.urls import path
from first_app import views
from django.urls import include

#this app_name is for template tagging
app_name = "first_app"
#without the abve namespace we cannot use the template tag that is used in the relative_url_templates.html
urlpatterns = [
    path("",views.index,name="index"),
    path("relative/",views.relative,name="relative"),
    path("other/",views.other,name="other"),
]
