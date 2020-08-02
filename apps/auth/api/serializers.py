from django.contrib.auth import get_user_model,  password_validation
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth import authenticate

User = get_user_model()



class AuthenticateUserSerializers(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    def validate(self, value):
        try:
            user = User.objects.get(email=value['email'])
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid username/password. Please try again!")
        else:
            if user.check_password(value['password']):
                return user
        raise serializers.ValidationError("Invalid username/password. Please try again!")
    

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)



class AuthUserSerializer(serializers.ModelSerializer):
    auth_token = serializers.SerializerMethodField()

    class Meta:
         model = User
         fields = ('id', 'email', 'first_name', 'last_name', 'auth_token')
         read_only_fields = ('id',)

    def get_auth_token(self, obj):
        token = Token.objects.get_or_create(user=obj)
        if isinstance(token, tuple):
            return token[0].key
        else:
            return token.key

class EmptySerializer(serializers.Serializer):
    pass





class UserRegisterSerializer(serializers.ModelSerializer):
    """
    A user serializer for registering the user
    """
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name',
                   'last_name', )
        read_only_fields = ('id',)
           

    def validate_email(self, value):
        user = User.objects.filter(email=value)
        if user:
            raise serializers.ValidationError("Email is already taken")
        return BaseUserManager.normalize_email(value)

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value

    def create(self, validate_data):
        user = get_user_model().objects.create_user(
        email=validate_data['email'], password=validate_data['password'], first_name=validate_data['first_name'],
        last_name=validate_data['last_name'])
        print(user)
        return user


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError('Current password does not match')
        return value

    def validate_new_password(self, value):
        password_validation.validate_password(value)
        return value