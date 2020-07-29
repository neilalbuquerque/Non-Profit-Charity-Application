from django.shortcuts import render
from my_donation_data.models import DonationForm
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.urls import reverse

# Create your views here.
def home(request):
	return render(request,'my_donation_data/home.html')

def ourwork(request):
	return render(request,'my_donation_data/ourwork.html')

def donateus(request):
	return render(request,'my_donation_data/donateus.html')

def donation_form_submit(request):
    if request.method == "POST":
        full_name = request.POST['full_name']
        email_id = request.POST['email_id']
        contact_number = request.POST['contact_number']
        donation = request.POST['donation']
        message = request.POST['message']
        DonationForm.objects.create(full_name=full_name,
                                   email_id=email_id,
                                   contact_number=contact_number,
                                   donation=donation,
                                   message=message
                                   )
    return HttpResponseRedirect(reverse('my_donation_data:donateus'))
