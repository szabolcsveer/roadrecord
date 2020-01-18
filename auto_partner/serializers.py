from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from auto_partner.models import Auto, Partner, AutoPartnerRelation
class AutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = '__all__'