from rest_framework import generics

from app.serializers import EmailSerializer
from app.models import Email


class EmailList(generics.ListCreateAPIView):

    queryset = Email.objects.all().order_by('-created')[:10]
    serializer_class = EmailSerializer
