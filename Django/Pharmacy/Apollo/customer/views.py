from django.shortcuts import render,redirect
from django.urls import reverse_lazy,reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from customer.forms import User_Signup,Create_med_form,Edit_med_form
from django.contrib.auth.models import User
from customer.models import Medicine
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView 
from django.contrib.auth.decorators import login_required,user_passes_test
# Create your views here.

def home(request):

    return render(request,"customer/home_page.html",{})

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user  = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home_link')

        else:
            messages.success(request,"User Not Found or Incorrect Password")
            return redirect("login_link") 
    else:
        return render(request,"customer/login_page.html",{})

def log_out(request):
    logout(request)
    return redirect("login_link")

# signup
def signup_user(request):
    if request.method == "POST":
        form = User_Signup(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            firstname = form.cleaned_data["firstname"]
            lastname = form.cleaned_data["lastname"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            if User.objects.filter(username=username).exists():
                form = User_Signup(request.POST)
                context = {
                    "form":form,
                    "error":"Username already exists"
                }

                return render(request,"customer/sign_up.html",context=context)

            if User.objects.filter(email=email).exists():
                form = User_Signup(request.POST)
                context = {
                    "form":form,
                    "error":"Email already exists"
                }

                return render(request,"customer/sign_up.html",context=context)
            else:
                user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name = firstname,
                last_name = lastname,
                )

                user.save()

                return redirect("login_link")        
        else:
            form = User_Signup(request.POST)
            context = {"form":form}
            return render(request,"customer/sign_up.html",context=context)

    else:
        form = User_Signup(request.POST)
        context = {"form":form}
        return render(request,"customer/sign_up.html",context=context)




# medic list
@login_required(login_url=reverse_lazy("login_link"))
def list_med(request):

    medic = Medicine.objects.filter(main_user = request.user)

    return render(request,"customer/med_list.html",{"medic":medic})

@login_required(login_url=reverse_lazy("login_link"))
def add_med(request):
    if request.method == "POST":
        form = Create_med_form(request.POST)

        if form.is_valid():
            med_name = form.cleaned_data["med_name"]
            med_price = form.cleaned_data["med_price"]
            disease = form.cleaned_data["disease"]

            medic_inst = Medicine(
                med_name=med_name,
                med_price=med_price,
                disease=disease,
                main_user = request.user

            )

            medic_inst.save()

            return HttpResponseRedirect(reverse("medic_list_link"))

        else:
            form = Create_med_form()
            return render(request,"customer/med_add.html",{"medform": form})
    else:
        form = Create_med_form()
        return render(request,"customer/med_add.html",{"medform": form})
              




# del medic

def del_med_conf(request,pk):

    med = Medicine.objects.get(pk=pk)

    return render(request,"customer/med_conf.html",{"med": med})


def del_medic(request,pk):

    medic = Medicine.objects.get(pk=pk)

    medic.delete()

    return HttpResponseRedirect(reverse("medic_list_link"))

# Edit Med

def edit_med(request,pk):
    if request.method == "POST":
        form = Edit_med_form(request.POST)

        if form.is_valid():
            med_name = form.cleaned_data["med_name"]
            med_price = form.cleaned_data["med_price"]
            disease = form.cleaned_data["disease"]

            medic_inst = Medicine.objects.get(pk=pk)

            medic_inst.med_name=med_name
            medic_inst.med_price = med_price
            medic_inst.disease = disease

            medic_inst.save()

            return HttpResponseRedirect(reverse("medic_list_link"))

        else:
            form = Edit_med_form(request.POST)
            return render(request,"customer/med_edit.html",{"editform": form})

    else:
        medic_inst = Medicine.objects.get(pk=pk)
        form = Edit_med_form(initial={"med_name":medic_inst.med_name,
                                       "med_price": medic_inst.med_price,
                                        "disease":medic_inst.disease})
        return render(request,"customer/med_edit.html",{"editform": form})

#search med 

def med_search(request):

    if request.method == "POST":
        searched=request.POST["searched"]

        res = Medicine.objects.filter(med_name__contains=searched)

        return render(request,"customer/med_search.html",{"searched":searched,"res":res})
    else:    
        return render(request,"customer/med_search.html",{"searched":searched,"res":res})