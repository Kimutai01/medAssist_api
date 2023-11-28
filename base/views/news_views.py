from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.models import New
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from base.serializer import NewSerializer
from rest_framework import status

@api_view(['GET'])
def getNews(request):
    news = New.objects.all()
    serializer = NewSerializer(news, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getNew(request, pk):
    new = New.objects.get(_id=pk)
    serializer = NewSerializer(new, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def createNew(request):
    user = request.user
    new = New.objects.create(
        user=user,
        title='Sample Name',
        category='Sample Category',
        description=''
    )
    serializer = NewSerializer(new, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateNew(request, pk):
    data = request.data
    new = New.objects.get(_id=pk)
    new.title = data['title']
    new.description = data['description']
    new.category = data['category']
    new.save()
    serializer = NewSerializer(new, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteNew(request, pk):
    new = New.objects.get(_id=pk)
    new.delete()
    return Response('New was deleted')

@api_view(['POST'])
def uploadImage(request):
    data = request.data
    news_id = data['news_id']
    new = New.objects.get(_id=news_id)

    new.image = request.FILES.get('image')
    new.save()

    return Response('Image was uploaded')

@api_view(['GET'])
def getOneLatestNew(request):
    new = New.objects.all().order_by('-_id')[:1]
    serializer = NewSerializer(new, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getNextFourLatestNews(request):
    new = New.objects.all().order_by('-_id')[1:5]
    serializer = NewSerializer(new, many=True)
    return Response(serializer.data)