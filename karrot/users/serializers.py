from django.contrib.auth import get_user_model
from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'username',
            'display_name',
        ]


class UserSerializer(serializers.ModelSerializer):
    photo_urls = VersatileImageFieldSerializer(sizes='user_profile', source='photo')

    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'username',
            'display_name',
            'photo_urls',
            'latitude',
            'longitude',
        ]


class UserProfileSerializer(serializers.ModelSerializer):
    photo_urls = VersatileImageFieldSerializer(sizes='user_profile', source='photo')

    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'username',
            'display_name',
            'email',
            'mobile_number',
            'address',
            'latitude',
            'longitude',
            'description',
            'photo_urls',
            'groups',
        ]
