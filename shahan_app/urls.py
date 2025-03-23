from django.urls import path
from .views import index,about,resume,services,portfolio,contact,packages

urlpatterns = [
    path('', index, name="index"),
    path('about/',about,name="about"),# Loads the HTML page at the root URL
    path('resume/',resume,name="resume"),
    path('services/',services,name="services"),
    path('portfolio/',portfolio,name="portfolio"),
    path('contact/',contact,name="contact"),
    path('packages/',packages,name="packages"),
    
    # Loads the HTML page at the root URL
# Loads the HTML page at the root URL
# Loads the HTML page at the root URL

]