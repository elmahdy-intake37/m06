from rest_framework import serializers
from apps.products.models import ProductOne, ProductTwo
from apps.users.models import TrackUser, User

class ProductOneSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductOne
        fields = '__all__'

class ProductTwoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductTwo
        fields = '__all__'      




class TrackUserSerializers(serializers.Serializer):
    class Meta:
        model = TrackUser
        fields = '__all__'


    def create(self, validate_data):
        user = User.objects.get(email=self.initial_data['email'])
        track, _  = TrackUser.objects.get_or_create(user=user, most_views_usage_name=self.initial_data['most_views_usage_name'])
        track.count +=1
        track.save()
        return track