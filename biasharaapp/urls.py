
from django.contrib import admin
from django.urls import path
from biasharaapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('gallery/',views.images),
    path('about/',views.about),
    path('contact/',views.contact),
    path('collection/',views.collection),
]
