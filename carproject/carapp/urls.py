from django.urls import path,include
from carapp import views

urlpatterns = [
    path('',views.Homeview.as_view()),
    path('insertcontact',views.insertcontact,name="insertcontact"),
    path('insertapponment',views.insertapponment,name="insertapponment")
    
]
