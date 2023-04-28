from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Order
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login_url') #TO amke the view more secured
def addOrderView(request):
    form = OrderForm()
    template_name = 'crudapp/add.html'
    context = {'form': form}
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save() 
    return render(request, template_name, context)

@login_required(login_url='login_url')
def showOrderView(request):
    data = Order.objects.all()
    template_name = 'crudapp/show.html'
    context = {'obj': data}
    return render(request, template_name, context)

def updateOrderView(request, pk):  #pk = parameter
    #print("Value of pk:", pk)
    ord = Order.objects.get(id = pk)  #fetching record
    #print("ORD OBJECT:", ord)
    form = OrderForm(instance=ord)   #Record will be displayed in form
    template_name = 'crudapp/add.html'
    context = {'form': form}
    if request.method=="POST":   #ADD ORDER request for POST method
        form = OrderForm(request.POST, instance=ord) #instance=ord for the existing record
        if form.is_valid():
            form.save()
            return redirect('showorder_url')
    return render(request, template_name, context)

def deleteOrderView(request, pk):
    ord = Order.objects.get(id = pk)
    template_name = 'crudapp/confirm.html'
    context = {'data': ord}
    if request.method == "POST":
        ord.delete()
        return redirect('showorder_url')
    return render(request, template_name, context)
    
