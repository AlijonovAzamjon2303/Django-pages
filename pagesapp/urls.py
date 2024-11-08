from django.urls import path
from .views import  HomePageView, AboutPageView, AzamjonPageView, ProjectsPageView

urlpatterns = [
    path('projects/', ProjectsPageView.as_view(), name='projects'),
    path('azamjon/', AzamjonPageView.as_view(), name='Azamjon'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home')

]