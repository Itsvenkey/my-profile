from django.shortcuts import render,redirect

# Create your views here.

def hello(request):
    return render(request,'base/home.html')

def linkedin(request):
    return redirect('https://www.linkedin.com/in/itsvenkey')

def github(request):
    return redirect('https://github.com/Itsvenkey')

def dbcerti(reqeust):
    return redirect("https://coursera.org/share/0aaa355dbc214b831da5ace5ca9647c7")

def certificate1(reqeust):
    return redirect("https://coursera.org/share/27721e6e2505276091df7590ef36ced3")

def versioncontrol(reqeust):
    return redirect("https://coursera.org/share/9b639f6ebc211d171b25123b82ff0bc9")

def djangowebframework(reqeust):
    return redirect('https://coursera.org/share/fd424804b4dea29b13919fdc478a23fb')

def introbackend(request):
    return redirect("https://coursera.org/share/06cc1ec2d8bec4fe056c87080277f017")

def pythonprogramming(reqeust):
    return redirect("https://coursera.org/share/aad8d4a9582b4e000c06c99a9a55da19")