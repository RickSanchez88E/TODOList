# views.py
from django.shortcuts import render, redirect
from myapp.forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., send an email, save to database)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Add your form processing logic here
            print(f"Received message from {name} ({email}): {message}")
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

