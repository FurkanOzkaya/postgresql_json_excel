from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from core.models import Data, Column
from core.api.serializer import ColumnSerializer, DataSerializer


class DataView(APIView):
    def get_object(self, pk):
        try:
            return Data.objects.get(id=pk)
        except:
            return "no_content"

    def get(self, request):
        try:
            columns = Column.objects.all()
            datas = Data.objects.all()
            serializered_column = ColumnSerializer(columns, many=True)
            serializered_data = DataSerializer(datas, many=True)
            print(serializered_column.data)
            response_json = {"column":serializered_column.data, "data":serializered_data.data}
            return Response(response_json, status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e), status=status.HTTP_204_NO_CONTENT)
    
    def post(self, request):
        serializer = DataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        print(pk)
        data = self.get_object(pk)
        if type(data) == str:
            return Response(status=status.HTTP_204_NO_CONTENT)
        try:
            serializer = DataSerializer(data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        data = self.get_object(pk)
        if type(data) == str:
            return Response(status=status.HTTP_204_NO_CONTENT)
        data.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

class ColumnView(APIView):
    def post(self, request):
        serializer = ColumnSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
