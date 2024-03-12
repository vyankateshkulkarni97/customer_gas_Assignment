# gas_utility_app/views.py
from django.shortcuts import render, redirect
from .models import ServiceRequest   , CustomerAccount
from django.contrib.auth.decorators import login_required
from .forms import ServiceRequestForm , CustomerAccountForm

# @login_required
def manage_account(request):
    customer_account, created = CustomerAccount.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = CustomerAccountForm(request.POST, instance=customer_account)
        if form.is_valid():
            form.save()
            return redirect('manage_account')
    else:
        form = CustomerAccountForm(instance=customer_account)

    return render(request, 'customer_account.html', {'form': form})


# @login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            return redirect('request_tracking')
    else:
        form = ServiceRequestForm()
    
    return render(request, 'submit_request.html', {'form': form})

def request_tracking(request):
    user_requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'request_tracking.html', {'user_requests': user_requests})