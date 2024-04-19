
from rest_framework import generics
from .serializers import PersonSerializer
from .models import Person
from rest_framework import viewsets
# Create your views here.
class PersonViewSet(viewsets.ModelViewSet):
  queryset = Person.objects.all()
  serializer_class = PersonSerializer