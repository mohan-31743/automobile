import re

from django.contrib.auth import authenticate
from django.db.models import Q
from django.utils import timezone

from .models import Registration, Feedback, product, categories, cart, payments
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
import random
import string
from django.contrib.auth.hashers import make_password
import time
from django.db.models import Subquery


def all(request):
    r = request.session["role"]
    u = request.session["username"]
    if r == 1:
        k=Registration.objects.all()
        p=payments.objects.all()
        return render(request, "all.html",{"user":k,"payments":p,"users":u})
    else:
        return render(request,"home.hrml")

def homepage(request):
    if 'username' in request.session:
        print(request.session['username'])
        r = request.session["role"]
        u = request.session["username"]
        if r == 1:
            k = Registration.objects.all()
            p = payments.objects.all()
            return render(request, "all.html", {"user": k, "payments": p,"users":u})
        return render(request, "home.html", {"msg": request.session['username']})
    else:
        return render(request, 'first.html')


def first1(request):
    if 'username' in request.session:
        r = request.session["role"]
        u = request.session["username"]
        if r == 1:
            k = Registration.objects.all()
            p = payments.objects.all()
            return render(request, "all.html", {"user": k, "payments": p,"users":u})
        print(request.session['username'])
        return render(request, "home.html",{"msg": request.session['username']})
    else:
        return render(request,'first.html')

def indexfunction(request):
    if 'username' in request.session:
        print(request.session['username'])
        return render(request, "home.html", {"msg": request.session['username']})
    else:
        return render(request, 'first.html')

def feedback(request):
    return render(request, "feedback.html")


def registration(request):
    return render(request, "registration.html")


def login(request):
    return render(request, "login.html")


def about(request):
    return render(request, "about.html")


def spares(request):
    return render(request, "spares.html")


def types(request):
    return render(request, "categories.html")


def slot(request):
    return render(request, "slot.html")


def checkloginfunction(request):
    email = request.POST["emailid"]
    pwd = request.POST["password"]

    if email == "pfsd@gmail.com" and pwd == "jsk":
        return homepage('home.html', homepage)
    else:
        return HttpResponse("<h1 color=white>Login Fail</h1>")


# Create your views here.
def addUserfunction(request):
    return render(request, "registration.html")

def cp(request):
    r = request.session["role"]
    user = request.session["username"]
    if r == 1:
        return render(request, "createproduct.html",{"username":user})
    else:
        return HttpResponse("Not Authorized")
def addproductfunction(request):
    return render(request,"spares.html")
def saveUserfunction(request):
    name = request.POST["name"]
    email = request.POST["email"]
    username = request.POST["username"]
    password = request.POST["password"]
    userobj = Registration(name=name, email=email, username=username, password=password)
    if re.search(r'[A-Z]', password):
        if re.search(r'[a-z]', password):
            if re.search(r'[!@#$%^&*()\-_=+{};:,<.>/?\[\]\\\|`~]', password):
                Registration.save(userobj)
                request.session["username"] = username
                request.session["role"] = 0
                return redirect("/")
            else:
                return HttpResponse("Registration failed !")
        else:
            return HttpResponse("Registration failed !")
    else:
        return HttpResponse("Registration failed !")


def savefeedbackfunction(request):
    name = request.POST["name"]
    email = request.POST["email"]
    feedback = request.POST["feedback"]
    feedobj = Feedback(name=name, email=email, feedback=feedback)
    Feedback.save(feedobj)
    return render(request, "feedback.html")

def saveproductfunction(request):
    pid=request.POST["pid"]
    name = request.POST["name"]
    des = request.POST["des"]
    price=request.POST["price"]
    imgurl = request.POST["imgurl"]
    cid=request.POST["cid"]
    r = request.session["username"]
    proobj = product(pid=pid,name=name, des=des, imgurl=imgurl,price=price,cid=cid,created_by=r)
    product.save(proobj)
    return render(request, "pro_add_succ.html")
def up(request):
    r = request.session["role"]
    if r == 1:
        return render(request,"updateproduct.html")
    else:
        return HttpResponse("Not Authorized")

def updateproductfunction(request):
    pid = request.POST["pid"]
    name = request.POST["name"]
    des = request.POST["des"]
    price = request.POST["price"]
    imgurl = request.POST["imgurl"]
    cid=request.Post["cid"]
    flag = product.objects.filter(pid=pid)
    if flag:
        product.objects.filter(pid=pid).update(name=name,des=des,price=price,imgurl=imgurl,cid=cid)
    return render(request, "pro_add_succ.html")

def login(request):
    return render(request, "login.html")


def userlogin(request):

    username = request.POST["username"]
    password = request.POST["password"]
    print(make_password(password))
    flag = Registration.objects.filter(Q(username=username) & Q(password=password))
    print(flag)
    if flag:
        user = Registration.objects.get(username=username)
        request.session["username"] = user.username
        request.session["role"] = user.role
        r = request.session["role"]
        u = request.session["username"]

        Registration.objects.filter(username=username).update(last_login=timezone.now())
        if r == 1:
            k = Registration.objects.all()
            p = payments.objects.all()
            return render(request, "all.html", {"user": k, "payments": p, "users": u})
        return render(request, "home.html", {"msg": user.username})
    else:
        msg = "Login Failed"
        return render(request, "login.html", {"msg": msg})

def getproductfunction(request):
    userdata=product.objects.all()
    usercount=Registration.objects.count()
    return render(request,"spares.html",{"users":userdata,"count":usercount})


def orderprodfunction(request,pid):
    prod = product.objects.get(pid=pid)
    return render(request, "order.html", {"prod": prod})


def getsession(request):
    if 'username' in request.session:
        name = request.session['username']
        role=request.session['role']
        print(role)
        return HttpResponse(role)

    if 'fusername' in request.session:
        fname = request.session['fusername']
        return HttpResponse("f   "+fname);

def logout(request):
    if 'username' in request.session:
        del request.session['username']
    return render(request,"first.html")

def user_profile(request):
    if 'username' in request.session:
        username=request.session['username']
        user = Registration.objects.get(username=username)
        return render(request, 'user_profile.html', {"user":user})
def forgotpassword(request):
    return render(request,'my_password_reset_confirm.html')


def forgot_password(request):
    if request.method == 'POST':
        username = request.POST['username']
        # Check if the entered username exists in the Registrations table
        user = Registration.objects.filter(username=username).first()
        if user:
            # If it exists, generate an OTP and send it to the user's email
            otp = random.randint(100000, 999999)
            send_mail(
                'OTP for Password Reset',
                f'Your OTP for password reset is: {otp}',
                'login_tt@outlook.com',
                [user.email],
                fail_silently=False,
            )
            request.session['otp'] = otp
            request.session['otp_timestamp'] = time.time()
            request.session['fusername'] = username

            messages.success(request, 'An OTP has been sent to your email.')
            return redirect('otp_verification')
        else:
            messages.error(request, 'Username not found.')
    return render(request, 'forgot_password.html')

def otp_verification(request):
    if request.method == 'POST':
        otp = request.POST['otp']
        if otp == str(request.session.get('otp')):
            otp_timestamp = request.session.get('otp_timestamp')
            if time.time() - otp_timestamp > 300:
                messages.error(request, 'OTP expired. Please generate a new one.')
                return redirect('forgot_password')
            messages.success(request, 'OTP verified.')
            return redirect('new_password')
        else:
            messages.error(request, 'Invalid OTP.')
    return render(request, 'otp_verification.html')

def new_password(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            # Update the user's password in the Requirements table
            username = request.session.get('fusername')
            user = Registration.objects.get(username=username)
            if user:
                user.password = password
                user.save()
                messages.success(request, 'Password updated successfully.')
                return redirect('login')
            else:
                messages.error(request, 'An error occurred.')
        else:
            messages.error(request, 'Passwords do not match.')
    return render(request, 'new_password.html')

def addcategoryfunction(request):
    cid=request.POST["cid"]
    name = request.POST["name"]
    imgurl = request.POST["imgurl"]
    r = request.session["username"]
    proobj = categories(name=name, imgurl=imgurl,cid=cid,created_by=r)
    categories.save(proobj)
    return render(request, "pro_add_succ.html")

def addcategory(request):
    r=request.session["role"]
    if r==1:
        return render(request, "createproduct.html")
    else:
        return HttpResponse("Not Authorized")



def getcategoryfunction(request):
    cdata=categories.objects.all()
    ccount=categories.objects.count()
    return render(request,"categories.html",{"categories":cdata,"count":ccount})

def viewcategoryproductfunction(request,pid):
    cat =product.objects.filter(cid=pid)
    return render(request, "spares.html", {"users": cat})

def view_cart(request):
    username=request.session["username"]
    cart_items = cart.objects.filter(user=username)
    print(cart_items.count())
    products = product.objects.filter(pid__in=Subquery(cart_items.values('productid')))
    print(products.count())
    total = sum([product.price for product in products])
    w=Registration.objects.get(username=username)
    return render(request, 'cart.html',{"products":products,"total_price":total,"total_items":products.count(),"wallet":w.wallet})

def add_cart(request):
    user=request.session["username"]
    prid=request.POST["pid"]
    cartobj=cart(user=user,productid=prid)
    cart.save(cartobj)
    return redirect('/cart')

def add_payment(request,id,price):
    user=request.session["username"]
    payobj=payments(user=user,payid=id,amount=price,paid_to="paypal")
    payments.save(payobj)
    pay = payments.objects.filter(user=user)
    payobj = payments(user=user, payid=id, amount=price,created_at=0)
    cart.objects.filter(user=user).delete()
    return render(request, 'payments.html', {"pay": pay,"paye":payobj,"msg":"Thank you. Your order has been received.","msg2":"Payment Successfull","mode":"Wallet"})


def showpayment(request):
    user = request.session["username"]
    pay=payments.objects.filter(user=user)
    payobj = payments(user="-", payid="-", amount="-",created_at="-")
    return render(request, 'payments.html', {"pay": pay,"paye":payobj,"msg":"You Previous Payments","msg2":"Payments"})

def deletecart(request):
    user = request.session["username"]
    cart.objects.filter(user=user).delete()
    return redirect('cart')

def allproducts(request):
    r = request.session["role"]
    user = request.session["username"]
    if r == 1:
        k=product.objects.all()
        p=categories.objects.all()
        return render(request,'allproducts.html',{"cat":p,"prod":k,"users":user})
    else:
        return HttpResponse("Not Authorized")


def updaterole(request,pid,rid):
    Registration.objects.filter(username=pid).update(role=rid)
    return redirect('/')

def deleteuser(request,uid):
    Registration.objects.filter(id=uid).delete()
    return redirect("/")

def deleteprod(request,uid):
    product.objects.filter(pid=uid).delete()
    return redirect("/viewproducts")

def deletecat(request,uid):
    Registration.objects.filter(cid=uid).delete()
    return redirect("/viewproducts")

def addwallet_payment(request,id,price):
    user=request.session["username"]
    payobj=payments(user=user,payid=id,amount=price,paid_to="wallet")
    payments.save(payobj)
    w=Registration.objects.get(username=user)
    k = str(price)
    price=price+w.wallet
    Registration.objects.filter(username=user).update(wallet=price)
    w = Registration.objects.get(username=user)
    user = request.session["username"]
    l = payments.objects.filter(user=user)
    lp = l.filter(paid_to="wallet")
    return render(request,'wallet.html',{"p":w,"msg":"Payment of "+k+" is Successfull","l": lp})

def remwallet_payment(request):
    user=request.session["username"]
    pric=request.POST["price"]
    id="WALL"+''.join(random.choices(string.ascii_uppercase+string.digits, k=13))
    payobj=payments(user=user,payid=id,amount=pric,paid_to="wallet")
    payments.save(payobj)
    w=Registration.objects.get(username=user)
    price=w.wallet-int(pric)
    Registration.objects.filter(username=user).update(wallet=price)
    pay = payments.objects.filter(user=user)
    payobj = payments(user=user, payid=id, amount=pric,created_at=0)
    cart.objects.filter(user=user).delete()
    return render(request, 'payments.html', {"pay": pay,"paye":payobj,"msg":"Thank you. Your order has been received.","msg2":"Payment Successfull","mode":"Wallet"})

def wallet(request):
    user = request.session["username"]
    k=Registration.objects.get(username=user)
    l=payments.objects.filter(user=user)
    lp=l.filter(paid_to="wallet")
    return render(request,'wallet.html',{"p":k,"l":lp})


#gift cards in which the user can make make a gift card by paying with mm wallet or paypal a unique id an key is generated
#and saved in gift card database (have fields user who buyed,amount,amount,buyed on ,claim status,claimed by)_ when a user try to claim it ,it should verify whether the card is already claimed or not
#if the card is not claimed then the money will be added to wallet .
