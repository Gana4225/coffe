from django.http import HttpResponse
from django.shortcuts import render, redirect
import razorpay
from .models import *
from django.views.decorators.csrf import csrf_exempt
import random
from .utils import coffee_data

def home(request):
    if request.method == "POST":
        for_type = request.POST.get('form_type')
        if for_type == "indexf":
            xyz = request.POST.get('name')
            name = request.session['name'] = request.POST.get('nm')
            at = request.session["at"] = request.POST.get("amt")
            img = request.POST.get('image')
            qua = int(request.POST.get('quantity'))
            amount = int(at) * 100 * qua
            amount1 = amount//100
            client = razorpay.Client(auth=("rzp_test_fdXm1LWL9qmt0N", "7uhH9YraGtUn5tGMthG20A6L"))
            payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
            request.session["pid"] = payment['id']
            random_number = random.randint(100000, 999999)
            context = {'payment': payment, 'rand': random_number, 'name':name, 'price':at, 'amt':amount1, 'img': img, 'qua':qua, 'xyz':xyz}
            response = render(request, "payments/index.html", context)
            payment = None  # This removes payment from memory

            return response
        else:
            quantity = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            amount = request.POST.get('price')
            img = request.POST.get('image')
            nm = request.POST.get('name')
            return render(request, "payments/index.html", {'price': amount, 'img': img, 'nm': nm, 'qua':quantity})
    # 192.168.162.247


    return render(request,"payments/index.html")
@csrf_exempt
def success(request):
    if request.method == "POST":
        a = request.POST
        rand = request.POST.get('rand')
        payment_id = request.POST.get("payment_id")
        order_id = request.POST.get("order_id")
        utr = request.POST.get("utr")
        order_id = ""
        for key, val in a.items():
            if key == 'razorpay_order_id':
                order_id = val
                user = coff.objects.filter(pid=order_id).first()
                user.paid = True
                user.save()

        a = coff.objects.filter(pid=request.session.get('pid')).count()
        if a < 1:
            coffee = coff(name=request.session.get('name'),
                          amount=request.session.get('at'),
                          pid=request.session.get('pid'))
            coffee.save()
    return render(request,"payments/status.html", {'rand':rand, 'utr':utr, 'pay_id':payment_id})

def tt(request):
    return render(request, "payments/tt.html", {"coffee_list": coffee_data})


def about_page(request):
    return render(request, 'payments/about.html')


def contact_page(request):
    if request.method == 'POST':
        # Handle form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # You can use this information for email or database handling here
        print(f"Message from {name}, Email: {email} - Message: {message}")
        return render(request, 'payments/contact.html', {'message': 'Thank you for your message!'})
    return render(request, 'payments/contact.html')

def refund(request):
    return render(request, "payments/refund.html")

def soon(request):
    return render(request, "payments/soon.html")

@csrf_exempt
def ladmin(request):
    ousernm = "admin"
    opassw = "admin"
    if request.method == "POST":
        user = request.POST.get('usernm')
        passw = request.POST.get('passw')

        if passw == opassw:
            request.session['user'] = user
            return redirect('edit')
    if request.session.get('user'):
            if request.method == "GET":
                del request.session['user']

    return render(request, "payments/login.html")
def edit(request):
    if request.session.get('user'):
        if request.method == "POST":
            name = request.POST.get('name')
            price = request.POST.get("price")
            description = request.POST.get('description')
            image = request.FILES.get("image")
        try:
            cofffdata.objects.create(name=name,price=price,description=description,image=image)
        except Exception as e:
            print(e)
        if request.method == "GET":
            return render(request, "payments/edit.html")
        bbt = 2525
        return render(request, "payments/status.html", {"edit":bbt})
    return render(request, "payments/login.html")

