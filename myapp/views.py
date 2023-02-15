from django.shortcuts import render,redirect

# Create your views here.
from myapp.forms import TodoForm,TodoModelForm,RegistrationForm,LoginForm
from myapp.models import todos,Todos
from django.contrib import messages
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

def signin_required(fn):
    def wrapper(request,*args,**kw):
        if not request.user.is_authenticated:
            messages.error(request,"u must login to perform this action")
            return redirect("signin")
        else:
            return fn(request,*args,**kw)
    return wrapper
@method_decorator(signin_required,name="dispatch")
class TodocreateView(CreateView):
    model=Todos
    form_class=TodoModelForm
    template_name="add-todo.html"
    success_url=reverse_lazy("todo-list")

    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,"todo created")
        return super().form_valid(form)
    

@method_decorator(signin_required,name="dispatch")
class TodolistView(ListView):
    model=Todos
    context_object_name="todos"
    template_name="todo-list.html"

    def get_queryset(self):
        return Todos.objects.filter(user=self.request.user)
    
    

@method_decorator(signin_required,name="dispatch")
class Tododetailview(DetailView):
    model=Todos
    template_name="todo-detail.html"
    context_object_name="todo"
    pk_url_kwarg:str="id"

@method_decorator(signin_required,name="dispatch")
class TododeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Todos.objects.filter(id=id).delete()
        messages.success(request,"removed successfully")
        return redirect("todo-list")

@method_decorator(signin_required,name="dispatch")
class TodoeditView(UpdateView):

    model=Todos
    form_class=TodoModelForm
    template_name="todo-update.html"
    pk_url_kwarg:str="id"
    success_url=reverse_lazy("todo-list")

    def form_valid(self, form):
        messages.success(self.request,"todo changed")
        return super().form_valid(form)
    
            
class RegistrationView(View):

    def get(self,request,*args,**kw):
        form=RegistrationForm()
        return render(request,"registration.html",{"form":form})
    
    def post(self,request,*args,**kw):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,"registerd successfully")
            return redirect("signin")
        else:
            messages.error(request,"registration failed")
            return render(request,"registration.html",{"form":form})

class LoginView(View):

    def get(self,request,*args,**kw):
        form=LoginForm()
        return render(request,"login.html",{"form":form})

    def post(self,request,*args,**kw):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                return redirect("todo-list")
            else:
                messages.error(request,"login failed")
                return render(request,"login.html",{"form":form})
@signin_required
def signout(request,*args,**kw):
    logout(request)
    return redirect("signin")