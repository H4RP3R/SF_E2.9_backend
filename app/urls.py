from django.urls import path
from app.views import EmailList


app_name = 'app'
urlpatterns = [
    path('emails', EmailList.as_view(), name='email-list'),
]
