import requests

def send_message( email, subject, message ) :
    '''
    Send message to mailgun api as an admin
    email - the email that you are sending to
    subject - the title of the mail
    message - Well the content
    '''
    return requests.post(
        "https://api.mailgun.net/v3/actime.mx/messages",
        auth = ( "api", "key-93786709ada1dde6b5857ed681388ac8" ),
        data = {
            "from" : "Actime Admin <admin@actime.mx>",
            "to" : [ email, "restcontmx@gmail.com" ],
            "subject" : subject,
            "text" : message 
        }
    )
# End of send_message function