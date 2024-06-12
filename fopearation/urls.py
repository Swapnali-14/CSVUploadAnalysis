from django.urls import path
from django.urls import path
from .import views


urlpatterns=[

    path('',views.fileupload),
    path('upload',views.upload),
    path('view',views.view_details)


]