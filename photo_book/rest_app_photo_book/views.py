from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_app_photo_book.serializers import UserSerializer
from rest_app_photo_book.models import User

from controlers.model import Model

mod = Model()


@api_view(['POST', "GET"])
def sign_up(request):

    if request.method == 'GET':
        data = {"displayName": "asdfUk",
                "email": "asdfuk@com.com",
                "password": "Git_Good25",
                "repeatPassword": "Git_Good25"}

    elif request.method == 'POST':
        data = request.data

    """Process of signing up"""

    result = mod.sign_up(data["displayName"], data["email"], data["password"], data["repeatPassword"])
    return Response(result)


@api_view(['POST', "GET"])
def sign_in(request):

    if request.method == 'GET':
        data = {"email": "asdfuk@com.com",
                "password": "Git_Good25"}

    elif request.method == 'POST':
        data = request.data

    """Process of signing in"""

    result = mod.sign_in(data["email"], data["password"])
    return Response(result)


@api_view(['POST', "GET"])
def create_album(request):

    if request.method == 'GET':
        data = {"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFzZGZ1ayIsImlkIjoyfQ.MB1FGWMIfkfUsSMHZuwuG5_GAs4ItlE1j39QzwYbN1A",
                "username": "asdfuk",
                "folder_name": "newShit2"}

    elif request.method == 'POST':
        data = request.data

    """Process of signing in"""

    result = mod.create_album(data["token"], data["username"], data["folder_name"])
    return Response(result)


@api_view(['POST', "GET"])
def create_file(request):

    if request.method == 'GET':

        with open("D:\off_work_activity\Slice at depth 610.png", "rb", ) as file:
            u = file.read()

        image_dict = {"name": "img.png",
                      "description": "guerrilla shit and stuff",
                      "date": "now",
                      "file": u}

        data = {"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFzZGZ1ayIsImlkIjoyfQ.MB1FGWMIfkfUsSMHZuwuG5_GAs4ItlE1j39QzwYbN1A",
                "username": "asdfuk",
                "folder_name": "newShit",
                "image_dict": image_dict}

    elif request.method == 'POST':
        data = request.data

    """Process of signing in"""

    result = mod.create_file(data["token"], data["username"], data["folder_name"], data["image_dict"])
    return Response(result)


@api_view(['POST', "GET"])
def get_albums(request):

    if request.method == 'GET':

        data = {"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFzZGZ1ayIsImlkIjoyfQ.MB1FGWMIfkfUsSMHZuwuG5_GAs4ItlE1j39QzwYbN1A",
                "username": "asdfuk"}

    elif request.method == 'POST':
        data = request.data

    """Process of signing in"""

    result = mod.get_albums(data["token"], data["username"])
    return Response(result)


@api_view(['POST', "GET"])
def get_files_in_album(request):

    if request.method == 'GET':

        data = {"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFzZGZ1ayIsImlkIjoyfQ.MB1FGWMIfkfUsSMHZuwuG5_GAs4ItlE1j39QzwYbN1A",
                "username": "asdfuk",
                "album": "newShit"}

    elif request.method == 'POST':
        data = request.data

    """Process of signing in"""

    result = mod.get_files_in_album(data["token"], data["username"], data["album"])
    return Response(result)


@api_view(['POST', "GET"])
def change_album_name(request):

    if request.method == 'GET':

        data = {"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFzZGZ1ayIsImlkIjoyfQ.MB1FGWMIfkfUsSMHZuwuG5_GAs4ItlE1j39QzwYbN1A",
                "username": "asdfuk",
                "folder_name": "newShit2",
                "new_name": "newShit2234"}

    elif request.method == 'POST':
        data = request.data

    """Process of signing in"""

    result = mod.change_album_name(data["token"], data["username"], data["folder_name"], data["new_name"])
    return Response(result)


@api_view(['POST', "GET"])
def change_file_attribute(request):

    if request.method == 'GET':

        image_dict = {"name": "img2.png",
                      "description": "guerrilla just",
                      "date": "yesterday"}

        data = {"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFzZGZ1ayIsImlkIjoyfQ.MB1FGWMIfkfUsSMHZuwuG5_GAs4ItlE1j39QzwYbN1A",
                "username": "asdfuk",
                "folder_name": "newShit",
                "file_name": "img.png",
                "image_dict": image_dict}

    elif request.method == 'POST':
        data = request.data

    """Process of signing in"""

    result = mod.change_file_attributes(data["token"], data["username"], data["folder_name"], data["file_name"], data["image_dict"])
    return Response(result)


@api_view(['POST', "GET"])
def delete_files(request):

    if request.method == 'GET':

        data = {"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFzZGZ1ayIsImlkIjoyfQ.MB1FGWMIfkfUsSMHZuwuG5_GAs4ItlE1j39QzwYbN1A",
                "username": "asdfuk",
                "folder_name": "newShit",
                "file_names": "img2.png"
                }

    elif request.method == 'POST':
        data = request.data

    """Process of signing in"""

    result = mod.delete_files(data["token"], data["username"], data["folder_name"], data["file_names"].split('#'))
    return Response(result)


@api_view(['POST', "GET"])
def delete_album(request):

    if request.method == 'GET':
        data = {"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFzZGZ1ayIsImlkIjoyfQ.MB1FGWMIfkfUsSMHZuwuG5_GAs4ItlE1j39QzwYbN1A",
                "username": "asdfuk",
                "folder_name": "newShit2"}

    elif request.method == 'POST':
        data = request.data

    """Process of signing in"""

    result = mod.delete_album(data["token"], data["username"], data["folder_name"])
    return Response(result)