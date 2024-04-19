from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
  is_adult = serializers.SerializerMethodField()
  class Meta:
    model = Person
    fields = [
      'name',
      'age',
      'is_adult'
    ]

  def get_is_adult(self,obj):
    
    print('hi there. I am being called')
    return obj.age >= 18