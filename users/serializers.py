from rest_framework import serializers

from . models import Profile
from django.contrib.auth.models import User
from . utils import sendMail

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","email"]

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSerializers
        fields = ["fullname","phone","gender","profile_pix"]

class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    username = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Profile
        fields = ["fullname","username","email","gender","password1","password2","gender","phone","profile_pix"]


    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("password not match")
        return data

    def create(self, validated_data):
        username = validated_data.pop('username')
        email = validated_data.pop('email') 
        password = validated_data.pop('password1')   

        user = User.objects.create_user(username=username,email=email,password=password)
        profile = Profile.objects.create(
            user=user,
            fullname = validated_data['fullname'],
            gender= validated_data['gender'],
            phone= validated_data['phone'],
            profile_pix= validated_data['profile_pix'],
            # this is how you create profile for a user.

        )

        sendMail(email)
        return profile

        # after creation of the user,profile and registration, there two things you only have to do
        # which is def create a user and validate
        # the validate is to validate the username,password,email. validate with create is an inbuilt function.
        # they are inbuilt functions that work on their own

        # for the create part, at times django don't let us use our own username, it gives us it's own username,
        # what we can do about that is change it to ours by doing
        # username = validated_data.pop('username')
        # email = validated_data.pop('email') 
        # the pop means what we're removing what was there before and putting ours
    