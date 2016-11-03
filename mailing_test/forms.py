from django import forms

class MailForm( forms.Form ) :
    email = forms.CharField( label = 'Email', max_length = 100 )
    message = forms.CharField( label = 'Message', max_length = 500 )
# End of mail form class