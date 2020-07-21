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
            html_message ='''<div><div></div><div tabindex="-1"></div><div><div><u></u><div style="margin:0!important;padding:0!important"> <img style="display:none!important"><table border="0" cellpadding="0" cellspacing="0" width="100%"><tbody><tr><td width="100%" align="center" valign="top" bgcolor="#eeeeee" height="20"></td></tr><tr><td bgcolor="#eeeeee" align="center" style="padding:0px 15px 0px 15px"><table bgcolor="#ffffff" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:600px"><tbody><tr><td><table width="100%" border="0" cellspacing="0" cellpadding="0"><tbody><tr><td align="center" style="padding:40px 40px 0px 40px"> <a href="#" target="_blank" data-saferedirecturl="#"> <img src="https://lh3.googleusercontent.com/VJqvoDVFn9X_oi8s2pVExiVhWeymDyBJaYl83ENKSyVFTeAHQ4inRKw-GoaiV4oMzIbOHA=s150" width="auto" border="0" style="vertical-align:middle"> </a></td></tr><tr><td align="center" style="font-size:18px;color:#0e0e0f;font-weight:700;font-family:Helvetica Neue;line-height:28px;vertical-align:top;text-align:center;padding:35px 40px 0px 40px"> <strong>'''+ subject + ''' </strong></td></tr><tr><td align="center" bgcolor="#ffffff" height="1" style="padding:40px 40px 5px" valign="top" width="100%"><table cellpadding="0" cellspacing="0" width="100%"><tbody><tr><td style="border-top:1px solid #e4e4e4"> <br> <br>Hi ''' + name + ''', <br> <br>Thank you for contacting us, Our team will get back soon to your request. <br>Your preferred choices are: <br> <br>PACKAGE : ''' + package +''' <br>PLAN : ''' + plan + ''' <br> <br> <strong>Regards <br> DEGnDEV </strong></td></tr></tbody></table></td></tr></tbody></table></td></tr><tr><td width="100%" align="center" valign="top" bgcolor="#ffffff" height="45"></td></tr></tbody></table></td></tr><tr><td bgcolor="#eeeeee" align="center" style="padding:20px 0px"><table width="100%" border="0" cellspacing="0" cellpadding="0" align="center" style="max-width:600px"><tbody><tr></tr><tr><td bgcolor="#eeeeee" align="center"><table width="100%" border="0" cellspacing="0" cellpadding="0" align="center" style="max-width:600px"><tbody><tr><td align="center" style="text-align:center;padding:10px 10px 10px 10px"><p>&#169;copyright @ 2020 Degndev</p></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table><div></div><div></div></div><div></div></div></div><div style="display:none"><div></div></div><div></div></div>''' ,
            fail_silently=False
        )

        messages.success(request,'Your message has been sucessfully sent.')

        # return HttpResponseRedirect('/admin')
        return redirect('/home')
        # return render(request,"contact/contact.html",{})
