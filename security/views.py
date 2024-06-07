from rest_framework import viewsets
from .models import SecurityRecord
from .serializers import SecurityRecordSerializer


# Create your views here.
class SecurityRecordViewSet(viewsets.ModelViewSet):
    queryset = SecurityRecord.objects.all()
    serializer_class = SecurityRecordSerializer
