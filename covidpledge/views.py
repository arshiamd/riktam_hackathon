from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request,'index.html')

def loginPage(request):
    return render(request,'login.html')

def registerPage(request):
    # if request.user.is_authenticated:
	#     return redirect('home')
    # else:
    #     form = UserCreationForm()
    #     if request.method == 'POST':
	# 		form = CreateUserForm(request.POST)
	# 		if form.is_valid():
	# 			form.save()
	# 			user = form.cleaned_data.get('username')
	# 			messages.success(request, 'Account was created for ' + user)

	# 			return redirect('login')

    return render(request,'register.html')

def contact(request):
    return render(request,'contactus.html')