from rest_framework import status
from rest_framework.response import Response
from .serializer import UserSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.contrib.auth import authenticate,login
from django.shortcuts import render



# from django.db.models import Q  For comparision

class RegisterApi(APIView):
    serializer_class = UserSerializer
    def post(self, request, *args,  **kwargs):
        username = request.data.get('username')
        email = request.data.get('email')

        # if User.objects.filter(Q(username=username) | Q(email=email)).exists():
        #     return Response({'error': 'Username or Email already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def get(self,request,pk=None):
        if pk:
            User_obj = User.objects.filter(id=pk).first()
            serializer = UserSerializer(User_obj)
            return Response({'status':200,'payload':serializer.data})
        else:
            User_obj = User.objects.all()
            serializer = UserSerializer(User_obj, many=True)
            return Response({'status':200,'payload':serializer.data})

class LoginApi(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # return Response({'status': 200}, template_name='main/index.html')
            return render(request, 'main/index.html')


            # return render(request, 'registration/token_send.html')

        else:
            return Response({'status': 403, 'payload': 'Failed'})

# class LoginApi(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         return Response({'status': 200, 'payload': 'Successful login'})
        