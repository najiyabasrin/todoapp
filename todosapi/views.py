from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response



class Todosview(ViewSet):
    
    def list(self,request,*args,**kw):
        return Response(data="list of todos")


    def create(self,request,*args,**kw):
        return Response(data=" todo created")


    def retrieve(self,request,*args,**kw):
        return Response(data="detail of a todo")


    def update(self,request,*args,**kw):
        return Response(data="updating todo")


    def destroy(self,request,*args,**kw):
        return Response(data="todo-deleted")

    
    


    