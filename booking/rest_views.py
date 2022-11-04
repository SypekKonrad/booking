from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from .serializers import *

from booking.models import *


class MakeListView(ListCreateAPIView):
    queryset = Make.objects.all()
    serializer_class = MakeSerializer
    permission_classes = [AllowAny]

class ModelListView(ListCreateAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer
    permission_classes = [AllowAny]