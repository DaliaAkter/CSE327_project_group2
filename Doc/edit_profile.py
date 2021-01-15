from django.shortcuts import render

"""
EDIT-PROFILE FUNCTION DOCUMENTATION
___________________________________________________
"""

# Create your views here.
def edit_profile(request):
    """
    This function will let the user update their profile information.
    To give access, it checks if user is authenticated.
    if 'True' user get access.
    if 'False' redirect to Login page.

    :param request: HTTP request-response protocol between a client and server.
    :param type: HTTP response.
    :return: returns the 'edit_profile.html' page  to authenticated user.

    """

  if not request.user.is_authenticated:
    return redirect('login')
    user = User.objects.get(id=request.user.id)
    data=Signup.objects.get(user=user)
    d={'data':data,'user':user}

    if request.method == 'POST':
        # post() sends a POST request to the specified url.
        # post() method sends data to the server.
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
