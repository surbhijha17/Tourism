
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login,logout,authenticate
from .forms import UserLoginForm,UserSignUpForm
from django.http import HttpResponseRedirect,HttpResponse ,JsonResponse

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.
def signup_view(request):
    if request.method =='POST':
        form=UserSignUpForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_active=True
            user.save()

            login(request,user)
            return redirect('home')
    else:
        form=UserSignUpForm()
    return render(request,'accounts/signup.html',{'form':form})


def login_view(request):
    if request.method =='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            if'next'in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('home')
    else:
        form= AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

#def login_view(request):
    if request.method =='POST':
        form=UserLoginForm(data=request.POST)
        if form.is_valid():
            username=request.POST["username"]
            password=request.POST["password"]
            user=authenticate(username=username,password=password)
            if user:
                if user.is_active():
                    login(request,user)
                    return HttpResponseRedirect(reverse('places:list'))
                else:
                    return HttpResponse("User is not active")
    else:
        form=UserLoginForm()
        return render(request,'accounts/login.html',{'form':form})
    #            if'next'in request.POST:
    #                return redirect(request.POST.get('next'))
    #            else:
    #                return redirect('articles:list')
    #    else:
    #        form= AuthenticationForm()
    #    return render(request,'accounts/login.html',{'form':form})

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('home')


def password_change_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('places:list')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/password_change.html', {
        'form': form
    })
