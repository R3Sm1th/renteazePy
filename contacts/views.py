from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        email = request.POST['email']
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        agent_email = request.POST['agent_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_is=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an enquiry')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, text=message, user_id=user_id)
        contact.save()

        messages.success(request, 'Your message has been submitted')

        return redirect('/listings/'+listing_id)
