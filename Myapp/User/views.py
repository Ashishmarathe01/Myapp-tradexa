
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.views.generic import DetailView,UpdateView,ListView,CreateView,DeleteView
from. models import Post


def singup(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if password == password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'User name Exist !')
                # SAME USERNAM
                return redirect('singup')

            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Eamil Exist ')

                    return redirect('singup')
                else:
                    #look good
                    user=User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password)
                    user.save()
                    # user created
                    return redirect('login')
        else:
            #doesnot match
            return redirect('singup')
    else:
        return render(request,'user/singup.html')



def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            #succefully login
            return redirect('l')
        else:
            messages.error(request,'Chek password and Username ')
            # not user
            return redirect('login')

    else:
        return render(request, 'user/login.html')           


        #CRUD
@login_required
def create(request):
    if request.method =='POST':
      text=request.POST['text']
      user=request.POST['user']
      print('text')
      u=User.objects.get(id=user)
      p=Post(text=text,user=u)
      p.save()
      messages.error(request,'post created ')

      return redirect('/l/')
    else:
        return render(request,'cb/c.html')  


class PostList(LoginRequiredMixin,ListView):
    model=Post
    template_name='cb/l.html'
    success_url='/l/'


class PostDetail(LoginRequiredMixin,DetailView):
    model=Post
    template_name='cb/d.html'
    success_url='/d/'   


class PostUpdate(LoginRequiredMixin,UpdateView):
    model=Post
    fields=['text']
    template_name='cb/u.html'
    success_url='/l/'     

class PostDele(LoginRequiredMixin,DeleteView):
    model=Post
    template_name='cb/dele.html'
    success_url='/l/'    

@login_required
def userLogout(request):
    logout(request)
    return redirect("/login/")
