from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Note
from .serializers import NoteSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    try:
        all_notes = Note.objects.all().order_by('-updated')
        all_notes_serialized = NoteSerializer(all_notes, many=True)
        return Response(all_notes_serialized.data, status=status.HTTP_200_OK)
    except:
        return Response('INVALID REQUEST', status=status.HTTP_404_NOT_FOUND) 

@api_view(['GET'])
def getNote(request, pk):
    try:
        note = Note.objects.get(id=pk)
        note_serialized = NoteSerializer(note, many=False)
        return Response(note_serialized.data)
    except:
        return Response('INVALID REQUEST', status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def updateNote(request, pk):
    try:
        data = request.data
        note = Note.objects.get(id=pk)
        note_serialized = NoteSerializer(instance=note, data=data)
        if note_serialized.is_valid():
            note_serialized.save()
        return Response(note_serialized.data)
    except:
        return Response('INVALID REQUEST', status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteNote(request, pk):
    try:
        note = Note.objects.get(id=pk)
        note.delete()
        return Response("DELETION SUCCESSFUL", status=status.HTTP_410_GONE)
    except:
        return Response("INVALID REQUEST", status=status.HTTP_400_BAD_REQUEST)



