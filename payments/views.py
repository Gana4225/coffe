from django.shortcuts import render
import razorpay
from .models import *
from django.views.decorators.csrf import csrf_exempt
import random

def home(request):
    if request.method == "POST":
        name = request.POST.get('nm')
        at = request.POST.get("amt")
        amount = int(at)*100
        client = razorpay.Client(auth=("rzp_test_fdXm1LWL9qmt0N","7uhH9YraGtUn5tGMthG20A6L"))
        payment = client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
        coffee = coff(name=name,amount=at,pid=payment['id'])
        coffee.save()
        random_number = random.randint(100000, 999999)
        context = {'payment': payment, 'rand':random_number}
        response = render(request, "index.html", context)
        payment = None  # This removes payment from memory

        return response
    return render(request,"payments/tt.html")
@csrf_exempt
def success(request):
    if request.method == "POST":
        a = request.POST
        rand = request.POST.get('rand')
        order_id = ""
        for key, val in a.items():
            if key == 'razorpay_order_id':
                order_id = val
                user = coff.objects.filter(pid=order_id).first()
                user.paid = True
                user.save()
    return render(request,"status.html", {'rand':rand})

def tt(request):
    amount = request.POST.get('price')
    img = request.POST.get('image')
    return render(request, "index.html", {'price':amount, 'img':img})
#192.168.162.247