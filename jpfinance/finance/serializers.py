from rest_framework import serializers
from finance.models import Finance

# Finance Serializer
class FinanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finance
        fields = '__all__'