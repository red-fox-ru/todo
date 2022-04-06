from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TodoSerializer


@api_view(['GET', 'POST', 'DELETE'])
def todo_list(request):
    if request.method == 'GET':
        todo = Task.objects.all()
        get_todo = TodoSerializer(todo, many=True)
        return Response(get_todo.data)

    elif request.method == 'DELETE':
        todo = Task.objects.filter(complete=True)
        todo.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'POST':
        post_todo = TodoSerializer(data=request.data)
        if post_todo.is_valid():
            post_todo.save()
            return Response(post_todo.data, status=status.HTTP_201_CREATED)
        return Response(post_todo.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TodoSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TodoSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
