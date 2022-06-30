from .models import MyUsers
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

class  SignUpSerializer(serializers.ModelSerializer) :    # SignIn Serializer
    
    username = serializers.CharField(
        required = True,
        validators = [UniqueValidator(queryset = MyUsers.objects.all())]
    )
    
    email = serializers.EmailField(
        required = True,
        validators = [UniqueValidator(queryset = MyUsers.objects.all())]
    )
    
    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password],
    )
    
    class Meta :
        model = MyUsers
        fields =  ('username','password', 'name','email','age','gender','image','num_go_to_store','time_to_go_to_store',)  
    
    """
    def validate(self, data) :
        if data['password'] != data['password2'] :
            raise serializers.ValidationError(
                {"password" : "password didn't match."}
            )
            
        return data
    """

    def create(self, validated_data) :
        
        user = MyUsers.objects.create_user(
            username = validated_data['username'],
            name = validated_data['name'],
            email = validated_data['email'],
            gender = validated_data['gender'],
            age = validated_data['age'],
            num_go_to_store = 2,
            time_to_go_to_store = 3,
        )
        
        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user = user) 
        return user

class SignInSerializer(serializers.Serializer):
    username = serializers.CharField(
        required = True,
    )
    
    password = serializers.CharField(
        required = True,
        write_only = True,
    )

    def validate(self, data):
        user = authenticate(**data)
        if user:
            token = Token.objects.get(user=user)
            return token
        raise serializers.ValidationError(
            {"error" : "Unable to log in with provided credentials."})


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUsers
        fields =  ('username', 'name','email','image')  