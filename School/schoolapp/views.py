from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from .models import User, Contact


# Create your views here.
def index(request):
    return render(request, "index.html")


def ragistration(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = make_password(request.POST["password"])
        if User.objects.filter(email=email).exists():
            messages.error(request, "your email exists in db")
        else:
            User.objects.create(name=name, email=email, password=password)
            return redirect("/login/")


def contactdetails(request):
    return render(request, "contact.html")


def contact1(request):
    if request.method == "POST":
        First_name = request.POST["firstname"]
        Last_name = request.POST["lastname"]
        Country_name = request.POST["country"]
        subject = request.POST["subject"]
        Contact.objects.create(
            First_name=First_name,
            Last_name=Last_name,
            Country_name=Country_name,
            subject=subject,
        )
        return redirect("/contact/")


def index1(request):
    return render(request, "login.html")


def login_user(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        if User.objects.filter(email=email).exists():
            obj = User.objects.get(email=email)
            password = obj.password

            if check_password(password, password):
                return redirect("/")
            else:
                messages.error, HttpResponse("password incurect")
                return redirect("/data/")

        else:
            messages.error(request, "email not register")
            return redirect("/")


def data(request):
    user = User.objects.all()
    return render(request, "data.html", {"user": user})


def table1(request):
    data = Contact.objects.all()
    return render(request, "table.html", {"data": data})


def delete_user(request, pk):
    User.objects.filter(id=pk).delete()
    return redirect("/data/")


def update(request, id):
    user = User.objects.get(id=id)
    return render(request, "update.html", {"user": user})


def update_data(
    request,
):
    if request.method == "POST":
        id = request.POST["id"]
        name = request.POST["name"]
        email = request.POST["email"]
        User.objects.filter(id=id).update(name=name, email=email)
        return redirect("/data/")
