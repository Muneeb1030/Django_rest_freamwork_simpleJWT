from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import get_db, MongoUser
from .serializers import UserSerializer
import json

from datetime import datetime, timezone

authenticator = JWTAuthentication()



@api_view(["GET"])
def get_user_all(request):
    db = get_db()
    session_token = request.META.get('HTTP_SESSION')
    if session_token:
        # Use the session_token to authenticate the request
        user = authenticator.get_validated_token(session_token)
        print(user)
        if user:
            # The user is authenticated, proceed with the request
            result = list(db.user.find({},{"_id":0}))
            return Response(result, status=status.HTTP_200_OK)
        else:
            # The user is not authenticated, return an error response
            return Response({'error': 'Invalid session token'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        # No session token was provided in the header
        return Response({'error': 'No session token provided'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(["DELETE"])
def delete_user_all(request):
    db = get_db()
    db.user.delete_many({})
    return Response({"Deleted": "All Users are deleted"})

@api_view(["POST"])
def create_user(request):
    db = get_db()
    user = request.data
    user = UserSerializer(data=user)
    if user.is_valid():
        user = user.validated_data
        user['date_joined'] = datetime.now(timezone.utc)
        result = db.user.insert_one(user)
        return Response({'Inserted': f'User with {result.inserted_id} is Added to record'}, status=status.HTTP_201_CREATED)
    return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def login(request):
    db = get_db()
    username = request.data.get('username')
    password = request.data.get('password')

    user_collection = get_db()
    user = user_collection.user.find_one({'username': username})
    print(user)
    print(type(user))
    if user and password == user['password']:
        user1 = MongoUser(user)
        refresh = RefreshToken.for_user(user1)
        user['token_access'] = str(refresh.access_token)
        user['token_refresh'] = str(refresh)

        db.user.update_one({'_id': user["_id"]}, {"$set":user})
        print(request.headers)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
    return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

