from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from . import serializers
from apps.users.models import TrackUser

class TrackUserViews(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):

    queryset = TrackUser.objects.all()
    serializer_class = serializers.TrackUserSerializers
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return self.queryset.filter(user__email=self.request.user).order_by('-count')

