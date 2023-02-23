from django.shortcuts import render
from customer.models import Medicine
from customer.forms import Create_med_form,Edit_med_form
from customerapi.serializer import list_med_serial
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from customerapi.forms import RegistrationForm
from django.contrib.auth import authenticate,login,logout
from rest_framework.decorators import api_view,permission_classes
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

#signup api
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def signup_api(request):
    register = RegistrationForm(request.data)

    if register.is_valid():
        username = register.cleaned_data["username"]
        firstname = register.cleaned_data["firstname"]
        lastname = register.cleaned_data["lastname"]
        email = register.cleaned_data["emailid"]
        password = register.cleaned_data["password"]

        if User.objects.filter(username=username).exists():
            register = RegistrationForm(request.POST)
            context = {"register":register.data,"Error":"username already exists"}
            return Response(context,status=HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            register = RegistrationForm(request.POST)
            context = {"register":register.data,"Error":"email already exists"}
            return Response(context,status=HTTP_400_BAD_REQUEST)

        else:
            user = User.objects.create_user(
                   username=username,
                   email=email,
                   password=password,
                   first_name = firstname,
                   last_name = lastname,
                )

            user.save()
            context = {"register":register.data,"success":"user create successfully"}
            return Response(context,status=HTTP_200_OK)
    else:
        register = RegistrationForm(request.POST)
        context = {"register":register.data,"Error":register.errors}
        return Response(context,status=HTTP_400_BAD_REQUEST)


# login api
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login_api(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if username is None or password is None:
        return Response({"error":"Please provide both username and password"},status=HTTP_400_BAD_REQUEST)

    user = authenticate(username=username,password=password)

    if not user:
        return Response({"error": "User not found"},status=HTTP_404_NOT_FOUND)

    token,_ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key},status=HTTP_200_OK)

# logout
@csrf_exempt
@api_view(["POST"])
def logout_api(request):
    request.user.auth_token.delete()

    return Response({"Sataus":"User Logout Successfully"},status=HTTP_200_OK)
    


# list_med
@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def list_med(request):
    user = request.user
    if not user.is_authenticated:
        return Response({"Error":"User Need To Login"},status=HTTP_400_BAD_REQUEST)

    else:
        medic_inst = Medicine.objects.filter(main_user = user)

        medic_inst_serial = list_med_serial(medic_inst,many=True)

        return Response(medic_inst_serial.data,status=HTTP_200_OK)    
    


@csrf_exempt
@api_view(["DELETE"])
@permission_classes((AllowAny,))
def del_med(request):
    medic_id = request.data.get("medic_id")
    user = request.user

    medic_inst = Medicine.objects.filter(id=medic_id,main_user=user)

    medic_inst.delete()

    return Response({"status":"Delete Sucessfully"},status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def search_med(request):
    med_search = request.data.get("search")
    user = request.user
    
    if Medicine.objects.filter(med_name=med_search).exists():

        medic_inst = Medicine.objects.filter(med_name=med_search,main_user=user)

        med_serial = list_med_serial(medic_inst,many=True)
    
        return Response(med_serial.data,status=HTTP_200_OK)

    else:
        return Response({"Result":"No Data Found"},status=HTTP_404_NOT_FOUND)   


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def add_med(request):

    form  = Create_med_form(request.data)

    if form.is_valid():
        med_name = form.cleaned_data["med_name"]
        med_price = form.cleaned_data["med_price"]
        disease = form.cleaned_data["disease"]

        med_inst = Medicine()

        med_inst.med_name = med_name
        med_inst.med_price = med_price
        med_inst.disease = disease
        med_inst.main_user = request.user

        med_inst.save()

        return Response({"Status":"Medicine Added Sucessfully"},status=HTTP_200_OK)

    else:
        form = Create_med_form(request.POST)
        return Response({"Status":"No Medicine Added"},status=HTTP_400_BAD_REQUEST)

        
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def update_med(request,pk):
    user = request.user
    if user.is_authenticated:
        med_inst = Medicine.objects.get(id=pk)
        med_serial = list_med_serial(instance=med_inst,data=request.data)

        if med_serial.is_valid():
            med_serial.save()

        return Response(med_serial.data,status=HTTP_200_OK)

    else:
        return Response(status=HTTP_400_BAD_REQUEST)          

    