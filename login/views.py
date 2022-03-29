from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

def loginView(request):
    if(request.POST):
        login_data = request.POST.dict()
        #print(login_data)
        name = login_data.get("identity")
        pssrw = login_data.get("password")
        user = authenticate(username=name, password=pssrw)
        if user is not None:
            print("**** AUTH SUCCEED ****")
            login(request,user)
            # next = request.POST.get('next', '/hub')
            # return redirect(next)
            return render(request, 'hub/hub.html')
        else:
            print("AUTH FAILED")
    
    else:
        logout(request)
        print("No post request")


    return render(request, 'login/form.html')


def logoutView(request):
    print("*** LOGOUT ***")
    logout(request)
    return redirect("/")
