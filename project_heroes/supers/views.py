from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Super

# Create your views here.

@api_view(['GET', 'POST'])
def super_list(request):

    if request.method == 'GET':

        supers = Super.objects.all()
        supers_filtered_heroes = supers.filter(hero = "Heroes")
        supers_filtered_villians = supers.filter(villian = "Villians")
        supers_heroes_serialized = SuperSerializer(supers_filtered_heroes, many = True)
        supers_villians_serialized = SuperSerializer(supers_filtered_villians, many = True)

        custom_dictionary = {"Heroes" : supers_heroes_serialized.data,
                            "Villians" : supers_villians_serialized.data,}
                    
    elif request.method == 'POST':

        print(request.data)
        serializer = SuperSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(custom_dictionary,status = status.HTTP_200_OK)

