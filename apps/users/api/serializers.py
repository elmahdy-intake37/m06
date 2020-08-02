from rest_framework import serializers
from apps.users.models import TrackUser


class TrackUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = TrackUser
        fields = '__all__'