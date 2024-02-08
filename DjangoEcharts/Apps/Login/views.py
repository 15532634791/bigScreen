from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.request import Request
from rest_framework import generics, status
from .models import User


class Login(TokenObtainPairView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            raise e

        result = serializer.validated_data
        result['id'] = serializer.user.id
        result['username'] = serializer.user.username
        result['date_joined'] = serializer.user.date_joined
        result['is_staff'] = serializer.user.is_staff
        result['token'] = result.pop('access')

        return Response(result, status=status.HTTP_200_OK)


class Register(APIView):

    permission_classes = []

    def post(self, request):
        # 1 接收用户参数
        username = request.data.get('username')
        password = request.data.get('password')
        password_confirmation = request.data.get('password_confirmation')

        # 2 校验参数
        if not all([username, password, password_confirmation]):
            return Response({'error': '所有参数不能为空'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': '用户名已存在'}, status=status.HTTP_400_BAD_REQUEST)

        if password != password_confirmation:
            return Response({'error': '两次输入都密码不一致'}, status=status.HTTP_400_BAD_REQUEST)

        if not (6 <= len(password) <= 18):
            return Response({'error': '密码需要在6到18位之间'}, status=status.HTTP_400_BAD_REQUEST)

        obj = User.objects.create_user(username=username, password=password)
        password = obj.password
        is_staff = obj.is_staff
        date_joined = obj.date_joined

        response = {
            'id': obj.id,
            'username': username,
            "password": password,
            "is_staff": is_staff,
            "date_joined": date_joined


        }

        return Response(response, status=status.HTTP_201_CREATED)