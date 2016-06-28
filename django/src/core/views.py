from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.models import User
from core.serializers import UserSerializer


@api_view(['GET', 'POST'])
def user_list(request, format=None):
    """
    List of users or new user
    """
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        response = Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            response = JSONResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            response = JSONResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return response

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk, format=None):
    """
    Retrieve an user, edit an user or delete an user
    """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        response = Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data)
        else:
            response = Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        response = HttpResponse(status=status.HTTP_204_NO_CONTENT)

    return response