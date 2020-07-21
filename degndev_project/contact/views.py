from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from . models import Contact
from pathlib import Path
from email.mime.image import MIMEImage
from django.core.mail import EmailMultiAlternatives


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        package = request.POST.get('package')
        plan = request.POST.get('plan')
        message = request.POST['message']

        contact = Contact(name=name, email=email, subject=subject, package=package, plan=plan, message=message )

        contact.save()

        # send send_mail
        send_mail(
            'DegnDev - Design and Development',
            'Hi ' + name + ', \n\nThank you for contacting us, Our team will get back soon to your request on ' + subject + ' with your preferred choice \n\nPACKAGE : ' + package + ' \nPLAN : ' + plan + '.' ,
            'degndev@gmail.com',
            recipient_list=[email,'degndev@gmail.com'],
            html_message = '''<table align="center" height="100%" width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#ffffff" style="font-family:Helvetica,Arial,sans-serif!important"><tbody><tr><td><table width=" 690" align="center" border="0" cellspacing="0" cellpadding="0"><tbody><tr bgcolor="#ffffff"><td align="center" width="100%"><table align="center" width="690" border="0" cellspacing="0" cellpadding="0"><tbody><tr><td width="100%" height="16" colspan="2"></td></tr><tr><td align="center" width="300"><a href="https://www.degndev.com" target="_blank" data-saferedirecturl="https://lh3.googleusercontent.com/VJqvoDVFn9X_oi8s2pVExiVhWeymDyBJaYl83ENKSyVFTeAHQ4inRKw-GoaiV4oMzIbOHA=s150"><img src="https://lh3.googleusercontent.com/VJqvoDVFn9X_oi8s2pVExiVhWeymDyBJaYl83ENKSyVFTeAHQ4inRKw-GoaiV4oMzIbOHA=s150" alt="DegnDev" border="0" width="150" style="display:block"></a></td></tr><tr><td width="100%" height="16" colspan="2"></td></tr></tbody></table></td></tr><tr><td align="center" width="100%"><table width="690" border="0" align="center" cellpadding="0" cellspacing="0" bgcolor="#eef2f5" style="border-radius:10px"><tbody><tr><td align="left" valign="top"><table width="560" align="center" border="0" cellspacing="0" cellpadding="0"><tbody><tr><td width="100%" height="56"></td></tr><tr><td align="center" width="100%" style="text-align:justify"><span style="color:#0e1724;text-decoration:none;font-size:20px;line-height:20px;font-family:Helvetica,Arial,sans-serif"><strong>Hi '''
            + name +
            '''</strong>,</span></td></tr><tr><td width="100%" height="24"></td></tr><tr><td align="center" width="100%" style="color:#0e1724;text-align:justify;font-family:Helvetica,Arial,sans-serif;font-size:16px;line-height:28px"><table width="100%" align="center" border="0" cellspacing="0" cellpadding="0"><tbody><tr><td> Thank you for contacting us, Our team will soon get to your request and provide you the valuable response as soon as possible. <br><br> SUBJECT: '''
            + subject +
            '''<br> PACKAGE: '''
            + package +
            '''<br> PLAN: '''
            + plan +
            '''<br></td></tr></tbody></table><table width="100%" align="justify" border="0" cellspacing="0" cellpadding="0"><tbody><tr><td><br> <strong>Best Regards, <br> <span style="font-size:20px">DegnDev</span></strong></td></tr></tbody></table></td></tr><tr><td width="100%" height="56"></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table> <table><td><tr><p style="text-align:center">&#169; copyright DEGnDEV<p></tr></td></table>''' ,

            fail_silently=False
        )

        messages.success(request,'Your message has been sucessfully sent.')

        # return HttpResponseRedirect('/admin')
        return redirect('/home')
        # return render(request,"contact/contact.html",{})
