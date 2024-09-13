# views.py
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template import Context, Template
from django.template.loader import get_template
from .forms import EmailForm
from .models import User
from django.conf import settings

def send_bulk_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            body_template = form.cleaned_data['body']  # Get the raw body with placeholders
            attachments = request.FILES.getlist('attachments')

            users = User.objects.all()

            # Send email to each user
            for user in users:
                # Render the email body using a Django template with user context
                template = Template(body_template)
                context = Context({'name': user.name})
                body = template.render(context)

                email_message = EmailMessage(subject, body, settings.DEFAULT_FROM_EMAIL, [user.email])

                # Add attachments to email
                for attachment in attachments:
                    email_message.attach(attachment.name, attachment.read(), attachment.content_type)

                email_message.content_subtype = 'html'  # If you want the email to be HTML-formatted
                email_message.send()

            return redirect('/')  # Redirect to a success page after sending the email
    else:
        form = EmailForm()

    return render(request, 'user/email_form.html', {'form': form})
