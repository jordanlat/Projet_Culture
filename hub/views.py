from django.shortcuts import redirect, render
from django.contrib.auth import logout

#@login_required(login_url='login')
def hubView(request):
    if request.user.is_authenticated:
        print("Welcome to The hub")
        print(request.user)
        return render(request,'hub/hub.html')
    else:
        print("Not auth!!")

def logoutView(request):
    print("**** LOGOUT ****")
    logout(request)
    return render(request,'login/login.html')


def goFilm(request):
    #print("go film !!!!!!")
    #return render(request, 'appfilms/appfilms.html')
    return redirect(request, 'films/')