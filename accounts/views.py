from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PlayerSerializer, UserSerializer
from .models import Player
from django.contrib.auth.models import User


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'get a specific user': '/user/',
        'modify friends': '/friends/',
        'modify chips': '/chips/',
        'modify gold': '/gold/',
    }
    return Response(api_urls)


@api_view(['GET'])
def user(request, famid):
    print(famid)
    q = famid.split()
    print(q)
    friendId = int(q[0])
    myid = int(q[1])
    nfriend = User.objects.get(pk=friendId)
    me = Player.objects.get(owner=myid)
    me.friends.add(nfriend)
    serializer = PlayerSerializer(me)
    return Response(serializer.data)


@api_view(['GET'])
def userAndPlayer(request, id):
    user = User.objects.get(pk=id)
    player = Player.objects.get(owner=id)
    serializer1 = PlayerSerializer(player)
    serializer2 = UserSerializer(user)
    return Response([serializer2.data, serializer1.data])


@api_view(['GET'])
def userRemove(request, famid):
    print(famid)
    q = famid.split()
    print(q)
    friendId = int(q[0])
    myid = int(q[1])
    nfriend = User.objects.get(pk=friendId)
    me = Player.objects.get(owner=myid)
    me.friends.remove(nfriend)
    serializer = PlayerSerializer(me)
    return Response(serializer.data)


@api_view(['GET'])
def addGold(request, magld):
    q = magld.split()
    myid = int(q[0])
    gol = int(q[1])
    moir = Player.objects.get(owner=myid)
    me = Player.objects.filter(owner=myid).update(gold=moir.gold + gol)
    moir = Player.objects.get(owner=myid)
    serializer = PlayerSerializer(moir)
    return Response(serializer.data)


@api_view(['GET'])
def rmGold(request, magld):
    q = magld.split()
    myid = int(q[0])
    gol = int(q[1])
    moir = Player.objects.get(owner=myid)
    me = Player.objects.filter(owner=myid).update(gold=moir.gold - gol)
    moir = Player.objects.get(owner=myid)
    serializer = PlayerSerializer(moir)
    return Response(serializer.data)


@api_view(['GET'])
def addChips(request, magld):
    q = magld.split()
    myid = int(q[0])
    chip = int(q[1])
    moir = Player.objects.get(owner=myid)
    me = Player.objects.filter(owner=myid).update(chips=moir.chips + chip)
    moir = Player.objects.get(owner=myid)
    serializer = PlayerSerializer(moir)
    return Response(serializer.data)


@api_view(['GET'])
def rmChips(request, magld):
    q = magld.split()
    myid = int(q[0])
    chips = int(q[1])
    moir = Player.objects.get(owner=myid)
    me = Player.objects.filter(owner=myid).update(chips=moir.chips - chips)
    moir = Player.objects.get(owner=myid)
    serializer = PlayerSerializer(moir)
    return Response(serializer.data)
