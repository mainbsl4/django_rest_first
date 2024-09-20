from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from myapp.models import ContractModal
from myapp.serializers import ContactSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import 


# Create your views here.


# class-based views Using mixins
class DataList(
    generics.ListCreateAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = ContractModal.objects.all()
    serializer_class = ContactSerializer

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DataDetail(
    generics.RetrieveUpdateDestroyAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = ContractModal.objects.all()
    serializer_class = ContactSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# # Rewriting our API using class-based views
# class DataList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """

#     def get(self, request, format=None):
#         allData = ContractModal.objects.all()
#         serializer = ContactSerializer(allData, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = ContactSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class DataDetail(APIView):

#     def get_object(self, pk):
#         try:
#             return ContractModal.objects.get(pk=pk)
#         except ContractModal.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = ContactSerializer(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = ContactSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# # Requests and Responses
# @api_view(["GET", "POST"])
# def data_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == "GET":
#         allData = ContractModal.objects.all()
#         serializer = ContactSerializer(allData, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = ContactSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["GET", "PUT", "DELETE"])
# def data_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         data = ContractModal.objects.get(pk=pk)
#     except data.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = ContactSerializer(data)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         serializer = ContactSerializer(data, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         ContractModal.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     # @csrf_exempt


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Serialization
# @csrf_exempt
# def data_list(request):

#     if request.method == "GET":
#         all_data = ContractModal.objects.all()
#         serializer = ContactSerializer(all_data, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = ContactSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# @csrf_exempt
# def data_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         data = ContractModal.objects.get(pk=pk)
#     except ContractModal.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == "GET":
#         serializer = ContactSerializer(data)
#         return JsonResponse(serializer.data)

#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = ContactSerializer(data, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == "DELETE":
#         ContractModal.delete()
#         return HttpResponse(status=204)
