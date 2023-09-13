from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from . models import Person
from . serializers import PersonSerializer
from django.urls import reverse

# Create your views here.

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

# @api_view(['GET', 'POST'])
# def persons(request):
#     if request.method == 'GET':
#         person = Person.objects.all()
#         serializer = PersonSerializer(person, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = PersonSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def person_detail(request, id):
#     person = get_object_or_404(Person, pk=id)
#     if request.method == 'GET':
#         serializer = PersonSerializer(person)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = PersonSerializer(person, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         person.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT) 

