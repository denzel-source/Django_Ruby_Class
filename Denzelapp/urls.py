# from Denzelapp.views import about
from django.urls import path
from Denzelapp import views
# from DjangoRubyClass_Project.urls import urlpatterns

urlpatterns =[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact, name='contact'),

    path('services/',views.services, name='services'),
    path('blogs/',views.blogs, name='blogs'),



]