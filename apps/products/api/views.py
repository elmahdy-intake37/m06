from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from . import serializers
from apps.products.models import ProductOne, ProductTwo
from rest_framework.response import Response
from apps.users.models import TrackUser
from django.urls import resolve

class ProductOneViews(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):

    queryset = ProductOne.objects.all()
    serializer_class = serializers.ProductOneSerializers
    permission_classes = [IsAuthenticated,]

    def list(self, request, *args, **kwargs):
        data = {'email': request.user, 'most_views_usage_name':  resolve(request.path).url_name}
        serializer = serializers.TrackUserSerializers(data=data)
        if serializer.is_valid():
             serializer.save()
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    




class ProductTwoViews(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):

    queryset = ProductTwo.objects.all()
    serializer_class = serializers.ProductTwoSerializers
    permission_classes = [IsAuthenticated,]

    def list(self, request, *args, **kwargs):
        data = {'email': request.user, 'most_views_usage_name':  resolve(request.path).url_name}
        serializer = serializers.TrackUserSerializers(data=data)
        if serializer.is_valid():
             serializer.save()
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
