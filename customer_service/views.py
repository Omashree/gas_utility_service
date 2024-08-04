from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest, Customer
from .forms import ServiceRequestForm, CustomerForm
from django.core.exceptions import ObjectDoesNotExist

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user.customer
            service_request.save()
            return redirect('track_requests')
    else:
        form = ServiceRequestForm()
    return render(request, 'customer_service/submit_request.html', {'form': form})

@login_required
def track_requests(request):
    service_requests = ServiceRequest.objects.filter(customer=request.user.customer)
    return render(request, 'customer_service/track_requests.html', {'service_requests': service_requests})

@login_required
def account_info(request):
    try:
        customer = request.user.customer
    except ObjectDoesNotExist:
        customer = Customer.objects.create(user=request.user)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('account_info')
    else:
        form = CustomerForm(instance=customer)
    