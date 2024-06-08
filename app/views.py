from django.shortcuts import render, redirect,get_object_or_404
from django.views import View
from .models import Contact
from django.contrib import messages
import requests
class IndexView(View):
    def get(self, request):
        contacts = Contact.objects.all()
        context = {'message': 'hello hello', 'contacts': contacts}
        return render(request, 'index.html', context)

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Create a new Contact object and save it
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        
        return redirect('index')  # Redirect to the index page after form submission


class EditContact(View):
    def get(self, request, pk):
        contact = get_object_or_404(Contact, pk=pk)
        return render(request, 'edit_contact.html', {'contact': contact})

    def post(self, request, pk):
        contact = get_object_or_404(Contact, pk=pk)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()
        
        messages.success(request, 'Contact updated successfully!')
        return redirect('index')  # Redirect to the index page after updating the contact


# class DeleteContact(View):
#     def get(self, request, pk):
#         contact = get_object_or_404(Contact, pk=pk)
#         return render(request, 'index.html', {'contact': contact})

#     def post(self, request, pk):
#         contact = get_object_or_404(Contact, pk=pk)
#         contact.delete()
#         messages.success(request, 'Contact deleted successfully!')
#         return redirect('index')  # Redirect to the index page after deleting the contact


# myapp/views.py


def api_contact(request):
    context = {}
    response = requests.get(url='http://localhost:8000/api/contact/')
    if response.status_code == 200:
        data = response.json()
        context = {'contacts': data}

    return render(request, 'api_contact.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Create a new Contact object and save it
        data = {
            'name':name,
            'email':email,
            'subject':subject,
            'message':message
        }
        response = requests.post(url='http://localhost:8000/api/contact/', data=data)
        if response.status_code == 201:
            messages.success(request, 'Contact created successfully!')
        return redirect('api_contact')  # Redirect to the index page after form submission
    return render(request,'contact.html')







def delete_contact(request, contact_id):
    if request.method == 'POST':
        # Delete the Contact object
        response = requests.delete(f'http://localhost:8000/api/contact/{contact_id}/')
        if response.status_code == 204:
            messages.success(request, 'Contact deleted successfully!')
        return redirect('api_contact')  # Redirect after deleting
    
    return render(request, 'delete_contact.html')




def update_contact(request, contact_id):
    # Fetch the existing contact details from the API
    response = requests.get(f'http://localhost:8000/api/contact/{contact_id}/')
    if response.status_code == 200:
        contact_data = response.json()
    else:
        messages.error(request, 'Contact not found!')
        return redirect('index')  # Redirect if contact not found
    
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Update the Contact object
        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }
        response = requests.put(f'http://localhost:8000/api/contact/{contact_id}/', data=data)
        if response.status_code == 200:
            messages.success(request, 'Contact updated successfully!')
        return redirect('api_contact')  # Redirect after updating
    
    return render(request, 'update_contact.html', {'contact': contact_data})
