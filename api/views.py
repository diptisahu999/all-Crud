from django.shortcuts import render
from .models import Student
from .serializer import Searial
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

# Create your views here.


## generic api

# class Listsss(generics.ListCreateAPIView):
#     queryset=Student.objects.all()
#     serializer_class=Searial
    
    
# class Listaaa(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Student.objects.all()
#     serializer_class=Searial
    
    
## function based api    
    
# @api_view(['GET','POST'])
# def list(request):
#     if request.method=='GET':
#         anc=Student.objects.all()
#         a=Searial(anc,many=True)
#         return Response(a.data)
    
#     elif request.method=="POST":
#         ss=Searial(data=request.data)
#         if ss.is_valid():
#             ss.save()
#             return Response(ss.data)
#         return Response(ss.errors)
    
    
# @api_view(["GET","PUT","DELETE"])
# def lists(request,pk):
#     ac=Student.objects.get(pk=pk)
#     if request.method=='GET':
#         a=Searial(ac)
#         return Response(a.data)
    
#      elif request.method=="PUT":
#         aaa=Searial(ac,data=request.data)
#         if aaa.is_valid():
#             aaa.save()
#             return Response(aaa.data)
#         return Response(aaa.errors)
    
    
#     elif request.method=="DELETE":
#         ac.delete()
#         return Response({'msg':'delete'})
    
#class based api    
class Listsss(APIView):
   
    def get(self,request,format=None):
        acc=Student.objects.all()
        ss=Searial(acc,many=True)
        return Response(ss.data)
    
    def post(self,request):
        s=Searial(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.errors)
    
    
class Listaaa(APIView):
   
    def get(self,request,pk):
        sa=Student.objects.get(pk=pk)
        ddd=Searial(sa)
        return Response(ddd.data)
    
    def put(self,request,pk):
        sa=Student.objects.get(pk=pk)
        dd=Searial(sa,data=request.data)
        if dd.is_valid():
            dd.save()
            return Response(dd.data)
        return Response(dd.errors)
    
    def delete(self,request,pk):
        sw=Student.objects.get(pk=pk)
        sw.delete()
        return Response({'msg':'delete'})
        
        
        
## viewsets api


# class ItemsViewSet(viewsets.ViewSet):

#     queryset = Student.objects.all()

#     def list(self, request):
#         serializer = Searial(self.queryset, many=True)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = Searial(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return render(serializer.data)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         item = get_object_or_404(self.queryset, pk=pk)
#         serializer = Searial(item)
#         return Response(serializer.data)
    
#     def delete(self, request, pk=None):
#         item = get_object_or_404(self.queryset, pk=pk)
#         # serializer = StudentSerializer(item)
#         item.delete()
#         return Response({'msg':'dta delete succefully'})
    
#     def put(self, request, pk=None):
#         item = get_object_or_404(self.queryset, pk=pk)
#         serializer = Searial(item,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return render(serializer.data)
#         return Response(serializer.errors)           



