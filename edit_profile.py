from django.shortcuts import render



# Create your views here.
def edit_profile(request):
    """
    this function will let the user update their profile information.

    """

  if not request.user.is_authenticated:
    return redirect('login')
    user = User.objects.get(id=request.user.id)
    data=Signup.objects.get(user=user)
    d={'data':data,'user':user}

    if request.method == 'POST':
         f=request.POST('firstname')
         l=request.POST('lastname')
         c=request.POST('contact')
         b=request.POST('branch')
         user.first_name= f
         user.last_name= l
         data.contact= c
         data.branch= b
         user.save()
         data.save()
         error=True
    d= {'data':data,'user':user,'error':error}
    return render(request,'edit_profile.html',d)
