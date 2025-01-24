from django.shortcuts import render
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def portfolio_home(request):
    """
    Renders the home page of the portfolio.
    """
    return render(request, 'index.html')


@csrf_exempt
def contact_form(request):
    """
    Handles contact form submissions. Accepts POST requests with name, email, subject, and message.
    Sends an email and returns a JSON response indicating success or failure.
    """
    if request.method == 'POST':
        try:
            # Parse JSON data from the request body
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            subject = data.get('subject')
            message = data.get('message')
            
            # Prepend "From Portfolio: " to the subject
            subject = f"From Portfolio: {subject}"
            
            # Create the email content
            email_message = f"Name: {name}\nEmail: {email}\n\nMessage: {message}"

            # Create an email message object
            email = EmailMessage(
                subject=subject,
                body=email_message,
                from_email=email,  # Use the sender's email from the form
                to=['aunychowdhury99@gmail.com'],  # Replace with your recipient email
                reply_to=[email],  # Set the reply-to address to the sender's email
            )

            # Send the email
            email.send(fail_silently=False)

            # Return success response
            return JsonResponse({'status': 'success', 'message': 'Email sent successfully!'})

        except Exception as e:
            # Log and return error response
            return JsonResponse({'status': 'error', 'message': f'Failed to send email: {str(e)}'})

    # Return error response for non-POST requests
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
