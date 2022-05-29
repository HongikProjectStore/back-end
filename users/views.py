from .models import MyUsers
from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import SignUpSerializer, SignInSerializer

# Create your views here.
class SignUpView(generics.CreateAPIView) :
    queryset = MyUsers.objects.all()
    serializer_class = SignUpSerializer

class SignInView(generics.GenericAPIView):
    serializer_class = SignInSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        return Response({"token":token.key}, status=status.HTTP_200_OK)