from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.models import Advert
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from base.serializer import AdvertSerializer
from rest_framework import status

@api_view(['GET'])
def getAdverts(request):
    adverts = Advert.objects.all()
    serializer = AdvertSerializer(adverts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAdvert(request, pk):
    advert = Advert.objects.get(_id=pk)
    serializer = AdvertSerializer(advert, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def createAdvert(request):
    user = request.user
    advert = Advert.objects.create(
        user=user,
        title='Sample Name',
        description=''
    )
    serializer = AdvertSerializer(advert, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateAdvert(request, pk):
    data = request.data
    advert = Advert.objects.get(_id=pk)
    advert.title = data['title']
    advert.description = data['description']
    advert.save()
    serializer = AdvertSerializer(advert, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteAdvert(request, pk):
    advert = Advert.objects.get(_id=pk)
    advert.delete()
    return Response('New was deleted')

@api_view(['POST'])
def uploadImage(request):
    data = request.data
    adverts_id = data['adverts_id']
    advert = Advert.objects.get(_id=adverts_id)
    
    advert.image = request.FILES.get('image')
    advert.save()

    return Response('Image was uploaded')