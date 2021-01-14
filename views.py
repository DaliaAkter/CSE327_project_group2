from django.shortcuts import render

# Create your views here.

def view_mynotes(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = user.objects.get(id=request.user.id)
    notes = note.objects.filter(user = user)
    d = {'notes':notes}
    return render(request,'view_mynotes.html',d)


def delete_mynotes(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    notes = Notes.objects.get(id=pid)
    notes.delete()
    return redirect('view_mynotes')


def view_users(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    users = Signup.objects.all()
    d = {'userss':notes}
    return render(request,'view_users.html',d)

def delete_users(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=pid)
    user.delete()
    return redirect('view_users')

