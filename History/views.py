from ast import And
from django.shortcuts import render
from django.http import HttpResponse
from .forms import logPage, changepassword
from .models import User

def getData(request):

    if request.method == 'POST':
        user_info = logPage(request.POST)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        pk = None
        if user_info.is_valid():
         print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
         N = user_info.cleaned_data.get('name')
         E = user_info.cleaned_data.get('email')
         P = user_info.cleaned_data.get('password')

         for user in User.objects.all():
            if user.name == N and user.email == E and user.password == P:
               pk = user.id

         if pk  != None:
            print("#######################################")
            return render(request, "History/thanks.html",{'user':N})      
          
          

         
        else:
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            return HttpResponse("No User Found")#render(request, "History/base.html", {'log_form': user_info})

    else:
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        form = logPage(None)

        return render(request, "History/base.html", {'log_form': form})


def change_password(request):

    if request.method == 'POST':
      form = changepassword(request.POST)
      if form.is_valid():

         new_password = form.cleaned_data.get('new_password')
         old_password = form.cleaned_data.get('old_password')
        
         reenter_password=form.cleaned_data.get('reenter_password')

         user = User.objects.get(password=form.cleaned_data.get('old_password'))
        
         

         if user.old_password == '':

            user.old_password = user.password
         else:
            user.old_password = user.old_password+','+user.password
         user.password = new_password
         user.save()
         return HttpResponse("Password Has been changed successfully")
      else:
        
         return HttpResponse("Unsuccess")

    else:
      a = changepassword(None)
      
      return render(request, "History/changepassword.html",{'changepasswordform':a})
