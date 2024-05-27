from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Athlete, CompleteInfo, BodySize, Disease
from .serializers import AthleteSerializer, CompleteInfoSerializer, BodySizeSerializer, DiseaseSerializer
from django.shortcuts import get_object_or_404


# Athlete View
class AthleteAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            athlete = get_object_or_404(Athlete, pk=pk)
            serializer = AthleteSerializer(athlete)
        else:
            athletes = Athlete.objects.all()
            serializer = AthleteSerializer(athletes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AthleteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        athlete = get_object_or_404(Athlete, pk=pk)
        serializer = AthleteSerializer(athlete, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        athlete = get_object_or_404(Athlete, pk=pk)
        athlete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# CompleteInfo View
class CompleteInfoAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            info = get_object_or_404(Athlete, pk=pk)
            serializer = CompleteInfoSerializer(info)
        else:
            infos = CompleteInfo.objects.all()
            serializer = CompleteInfoSerializer(infos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompleteInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        info = get_object_or_404(CompleteInfo, pk=pk)
        serializer = CompleteInfoSerializer(info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        info = get_object_or_404(CompleteInfo, pk=pk)
        info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# BodySize View
class BodySizeAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            size = get_object_or_404(BodySize, pk=pk)
            serializer = BodySizeSerializer(size)
        else:
            sizes = BodySize.objects.all()
            serializer = BodySizeSerializer(sizes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BodySizeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        size = get_object_or_404(BodySize, pk=pk)
        serializer = BodySizeSerializer(size, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        size = get_object_or_404(BodySize, pk=pk)
        size.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Disease View
class DiseaseAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            disease = get_object_or_404(Disease, pk=pk)
            serializer = DiseaseSerializer(disease)
        else:
            diseases = Disease.objects.all()
            serializer = DiseaseSerializer(diseases, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DiseaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        disease = get_object_or_404(Disease, pk=pk)
        serializer = DiseaseSerializer(disease, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        disease = get_object_or_404(Disease, pk=pk)
        disease.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
