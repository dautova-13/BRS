from rest_framework import serializers
from .models import *

class DisciplinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplines
        fields = ('id',
                  'name')
                  