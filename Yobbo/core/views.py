from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from .serializers import YobboAdminSerializer, PostSerializer
from .models import YobboAdmin, Post
import datetime
import jwt

# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        serializer = YobboAdminSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        yobboAdmin = YobboAdmin.objects.filter(email = email).first()
        
        if yobboAdmin is None: 
            raise AuthenticationFailed("User Not Found!")
        
        if not yobboAdmin.check_password(password):
            raise AuthenticationFailed("Incorrct Password!")
        
        payload = {
            'id' : yobboAdmin.id,
            'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat':datetime.datetime.utcnow()    
        }
        
        token = jwt.encode(payload, 'secret', algorithm='HS256')

        
        response = Response()
        response.data = {
            'jwt' : token
        }
        
        response.set_cookie(key = 'jwt', value = token, httponly = True)
        
        return response

class YobboAdminView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        
        if not token:
            raise AuthenticationFailed("Unauthenticated!!")
        
        try:
            payload = jwt.decode(token, 'secret', algorithms="HS256")
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated!!")
        
        yobboAdmin = YobboAdmin.objects.filter(id = payload['id']).first()
        serializer = YobboAdminSerializer(yobboAdmin)
        
        return Response(serializer.data)
    
class LogoutView(APIView):
    def post(self,request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message':'Successfully Logouted!!'
        }
        return response
    
class PostView(APIView):
    def post(self, request):
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
        