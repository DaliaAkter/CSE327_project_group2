from django.shortcuts import render

def pending_notes(request):
    #this function will show the new pending notes uploaded by the user.
 if not request.user.is_authenticated:
    return redirect('login_admin')
    notes = Notes.Objects.filter(status="pending")
    d= {'notes':notes}
    return  render(request,'pending_notes.html',d)
