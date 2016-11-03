from django.shortcuts import render
from .forms import MailForm
from . import mailing_helper

def send_mail( request ) :
    
    form = MailForm()
        
    if request.method == 'POST' :
        
        email = request.POST['email']
        message = request.POST['message']
        
        mailing_helper.send_message( email, 'test', message )
        
        context = {
            'message' : 'Your message has been send',
            'form' : form,
            'result' : { 'email' : email, 'message' : message }
        }
        
    else :
    
        context = {
            'message' : 'Hello World!!',
            'form' : form
        }
    
    return render( request, 'mail_form.html', context )
    