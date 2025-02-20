from django.shortcuts import render
import razorpay
from .models import *
from django.views.decorators.csrf import csrf_exempt
import random
from .utils import coffee_data

def home(request):
    if request.method == "POST":
        for_type = request.POST.get('form_type')

        if for_type == "indexf":
            name = request.POST.get('nm')
            at = request.POST.get("amt")
            img = request.POST.get('image')
            amount = int(at) * 100
            client = razorpay.Client(auth=("rzp_test_fdXm1LWL9qmt0N", "7uhH9YraGtUn5tGMthG20A6L"))
            payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
            coffee = coff(name=name, amount=at, pid=payment['id'])
            coffee.save()
            random_number = random.randint(100000, 999999)
            context = {'payment': payment, 'rand': random_number, 'name':name, 'price':at, 'img': img}
            response = render(request, "payments/index.html", context)
            payment = None  # This removes payment from memory

            return response
        else:
            amount = request.POST.get('price')
            img = request.POST.get('image')
            nm = request.POST.get('name')
            return render(request, "payments/index.html", {'price': amount, 'img': img, 'nm': nm})
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