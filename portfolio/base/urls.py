from django.urls import path
from . import views

urlpatterns = [
    path('',views.hello),
    path('linkedin/',views.linkedin),
    path('github/',views.github),
    path('intro-to-database-certificate/',views.dbcerti),
    path('contact-list-django-app-certificate/',views.certificate1),
    path('version-control-certificate/',views.versioncontrol),
    path('django-web-framework-certificate/',views.djangowebframework),
    path('intro-to-backend-development-certificate/',views.introbackend),
    path('programming-in-python-certificate/',views.pythonprogramming),
    
]