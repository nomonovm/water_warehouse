from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import *
from .models import *


class Mypagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100


class SuvListCreate(APIView):
    def get(self, request):
        suvlar = Suv.objects.all()
        serializer = SuvSerializer(suvlar, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SuvSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success": True,
                "message": "Suv muvafaqqiyatli qo'shildi!",
                "data": serializer.data
            }, status=201)
        return Response({"success": False, "message": "Xatolik!", "error": serializer.errors}, status=400)


class SuvRetrieveUpdateDeleteAPIView(APIView):
    def get(self, request, pk):
        suv = get_object_or_404(Suv, pk=pk)
        serializer = SuvSerializer(suv)
        return Response(serializer.data)

    def put(self, request, pk):
        suv = get_object_or_404(Suv, pk=pk)
        serializer = SuvSerializer(suv, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "message": "Yangilandi!", "data": serializer.data})
        return Response({"success": False, "message": "Xatolik!", "error": serializer.errors}, status=400)

    def delete(self, request, pk):
        suv = get_object_or_404(Suv, pk=pk)
        suv.delete()
        return Response({"success": True, "message": "O'chirildi!"}, status=204)


class MijozListCreate(APIView):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['ism', "tel"]
    search_fields = ['ism', 'tel']

    def get(self, request):
        serializer = MijozSerializer(Mijoz.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializers = MijozSerializer(data=request.data)
        if serializers.is_valid():
            data = serializers.validated_data
            Mijoz.objects.create(
                ism=data['ism'],
                manzil=data['manzil'],
                tel=data['tel'],
                qarz=data['qarz'],
            )
            res = {"succes": True, "messege": "Mijoz muvafaqqiyatli qo'shildi!", "data": serializers.data}
            return Response(res, status=201)
        res = {'succes': False, 'messege': 'Mijoz yaratilmadi!', 'error': serializers.errors}
        return Response(res, status=400)


class MijozRetrieveUpdateDeleteAPIView(APIView):
    def get(self, request, pk):
        mijoz = get_object_or_404(Mijoz, pk=pk)
        serializer = MijozSerializer(mijoz)
        return Response(serializer.data)

    def put(self, request, pk):
        mijoz = get_object_or_404(Mijoz, pk=pk)
        serializer = MijozSerializer(mijoz, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "message": "Mijoz yangilandi!", "data": serializer.data})
        return Response({"success": False, "message": "Xatolik!", "error": serializer.errors}, status=400)

    def delete(self, request, pk):
        mijoz = get_object_or_404(Mijoz, pk=pk)
        mijoz.delete()
        return Response({"success": True, "message": "Mijoz o'chirildi!"}, status=204)


class BuyurtmaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Buyurtma.objects.all()
    serializer_class = BuyurtmaSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['suv', 'mijoz']
    ordering_fields = ['sana']
    pagination_class = Mypagination


class HaydovchiListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        haydovchilar = Haydovchi.objects.all()
        serializer = HaydovchiSerializer(haydovchilar, many=True)
        return Response(serializer.data)


class SotuvchiListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        sotuvchilar = Sotuvchi.objects.all()
        serializer = SotuvchiSerializer(sotuvchilar, many=True)
        return Response(serializer.data)
