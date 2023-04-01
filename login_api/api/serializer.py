from rest_framework import  serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'first_name', 'last_name','email','password']

        extra_kwargs = {
            'username': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True},
            'password': {'required': True,'write_only':True},
            }
        
    def create(self, validated_data):
        user = User.objects.create(
            username= validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
 

#     def validate(self, data):
#         username = data.get('username')
#         password = data.get('password')

#         if not username or not password:
#             raise serializers.ValidationError('Username and password are required.')

#         user = authenticate(username=username, password=password)

#         if not user:
#             raise serializers.ValidationError('Invalid login credentials.')

#         if not user.is_active:
#             raise serializers.ValidationError('This user has been deactivated.')

#         data['user'] = user
#         return data



    
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
#         write_only_fields = ('password',)
#         read_only_fields = ('id',)

#     def create(self, validated_data):
#         user = User.objects.create(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             first_name=validated_data['first_name'],
#             last_name=validated_data['last_name']
#         )
#         user.set_password(validated_data['password'])
#         user.save()

#         return user