from django.shortcuts import render
from .forms import contactForm

# Create your views here.
def index(request):
    
    if request.method == 'POST':
        form = contactForm(request.POST)
        emails = []
        if form.is_valid():
            
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            
            message = form.cleaned_data['message']
            cc_myself = form.cleaned_data['cc_myself']    

            
            emails.append(email)
            print(email)
        print(emails)            
            
        return render(request,'examples/index.html',{'form':form})

    else:
        form = contactForm

    return render(request,'examples/index.html',{'form':form})



