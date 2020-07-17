from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from . models import Contact

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

        #send send_mail
        send_mail(
            'DegnDev - Design and Development',
            'Thank you for contacting us ' + name + ', Our team will get back soon to your response' + ' with your preferred PACKAGE : ' + package + ' and PLAN : ' + plan + ' ' ,
            'degndev@gmail.com',
            recipient_list=[email],
            # 'degndev@gmail.com'
            fail_silently=False
        )

        messages.success(request,'Your message has been sucessfully sent.')

        # return HttpResponseRedirect('/admin')
        return redirect('/home')
        # return render(request,"contact/contact.html",{})
