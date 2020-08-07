from app.models import Email
from rest_framework import serializers


class EmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Email
        fields = '__all__'
        read_only_fields = ('id', 'sent')
