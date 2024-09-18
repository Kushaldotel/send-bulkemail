# views.py
import asyncio
from django.shortcuts import render, redirect
from django.template import Context, Template
from aiosmtplib import send
from email.message import EmailMessage
from django.conf import settings
from asgiref.sync import sync_to_async
from .forms import EmailForm
from .models import User
from django.contrib.auth.decorators import login_required

# Async function to send individual emails using aiosmtplib
async def send_email_async(subject, body, recipient, attachments):
    message = EmailMessage()
    message["From"] = settings.DEFAULT_FROM_EMAIL
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body, subtype="html")

    # Add attachments
    for attachment in attachments:
        message.add_attachment(
            attachment['content'],
            filename=attachment['name'],
            maintype=attachment['content_type'].split('/')[0],
            subtype=attachment['content_type'].split('/')[1]
        )

    # Send the email asynchronously using aiosmtplib with STARTTLS
    await send(
        message,
        hostname=settings.EMAIL_HOST,
        port=settings.EMAIL_PORT,
        username=settings.EMAIL_HOST_USER,
        password=settings.EMAIL_HOST_PASSWORD,
        start_tls=True,  # Use STARTTLS for port 587 (Gmail)
    )

# Async function to send emails to all users
async def send_bulk_email_async(subject, body_template, users, attachments_data):
    tasks = []

    for user in users:
        # Render the email body using a Django template with user-specific context
        template = Template(body_template)
        context = Context({'name': user.name})
        body = template.render(context)

        tasks.append(send_email_async(subject, body, user.email, attachments_data))

    # Run the email sending tasks asynchronously
    await asyncio.gather(*tasks)

# Sync-to-async function to fetch users from the database
@sync_to_async
def fetch_users():
    return list(User.objects.filter(suscribed=True))

# Main view to handle the bulk email form and trigger async email sending
@login_required(login_url='/admin/login/')
def send_bulk_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            body_template = form.cleaned_data['body']
            attachments = request.FILES.getlist('attachments')

            # Prepare attachment data for async sending
            attachments_data = []
            for attachment in attachments:
                attachments_data.append({
                    'name': attachment.name,
                    'content': attachment.read(),
                    'content_type': attachment.content_type
                })

            # Fetch subscribed users asynchronously using sync_to_async
            users = asyncio.run(fetch_users())

            # Run the asynchronous email sending in an event loop
            asyncio.run(send_bulk_email_async(subject, body_template, users, attachments_data))

            return redirect('/')  # Redirect after successful sending
    else:
        form = EmailForm()

    return render(request, 'user/email_form.html', {'form': form})
