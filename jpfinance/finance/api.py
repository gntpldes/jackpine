from finance.models import Finance
from rest_framework import viewsets, permissions
from .serializers import FinanceSerializer

#Finance Viewset
class FinanceViewSet(viewsets.ModelViewSet):
    queryset = Finance.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FinanceSerializer