from rest_framework import generics

from app.serializers import EmailSerializer
from app.models import Email


class EmailList(generics.ListCreateAPIView):

    queryset = Email.objects.all()
    serializer_class = EmailSerializer
