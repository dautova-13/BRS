from rest_framework import serializers
from .models import *

class DisciplinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplines
        fields = ('id',
                  'name')
                  
class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = ('id',
                  'type_id',
                  'start_data',
                  'end_data',
                  'year')
        
class TypeTerm(serializers.ModelSerializer):
    class Meta:
        model = TypeTerm
        fields = ('id',
                  'name')
        
        
    
                  
                