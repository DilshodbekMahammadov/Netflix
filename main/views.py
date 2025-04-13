from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .models import *

class AktyorlarAPIView(APIView):
    def get(self, request):
        serializer = AktyorSerializer(Aktyor.objects.all(), many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = AktyorSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            Aktyor.objects.create(
                ism=data['ism'],
                davlat=data['davlat'],
                jins=data['jins'],
                t_sana=data['t_sana']
            )
            res = {
                'success' : True,
                'massage' : 'Aktyor muvaffaqiyatli qo\'shildi!',
                'data' : serializer.data
            }
            return Response(res, status=201)
        res = {
            'success' : False,
            'massage' : 'Aktyor yaratilmadi! Noto\'g\'ri so\'rov jo\'natoldi!',
            'errors' : serializer.errors
        }
        return Response(res, status=400)

class AktyorRetrieveUpdateDeleteAPIView(APIView):
    def get(self, request, pk):
        aktyor = Aktyor.objects.get(pk=pk)
        serializer = AktyorSerializer(aktyor)
        return Response(serializer.data)
    def put(self,request, pk):
        aktyor = Aktyor.objects.get(pk=pk)
        serializer = AktyorSerializer(aktyor)
        if serializer.is_valid():
            aktyor.ism = serializer.validated_data['ism']
            aktyor.davlat = serializer.validated_data['davlat']
            aktyor.jins = serializer.validated_data['jins']
            aktyor.t_sana = serializer.validated_data['t_sana']
            aktyor.save()
            res = {
                'success' : True,
                'massage' : 'Aktyor muvaffaqiyatli o\'zgartirildi!',
                'data' : serializer.data
            }
            return Response(res, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        aktyor = Aktyor.objects.get(pk=pk)
        aktyor.delete()
        return Response({"success": True, "massage" : "Aktyor o'chirildi!"}, status=204)

class TarifAPIView(APIView):
    def get(self, request):
        serializer = TarifSerializer(Tarif.objects.all(), many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = TarifSerializer(data = request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            Tarif.objects.create(
                nom=data['nom'],
                narx=data['narx'],
                davomiylik=data['davomiylik'],
                izoh=data['izoh']
            )
            res = {
                'success': True,
                'massage': 'Ta\'rif muvaffaqiyatli qo\'shildi!',
                'data': serializer.data
            }
            return Response(res, status=201)
        res = {
            'success': False,
            'massage': 'Ta\'rif yaratilmadi! Noto\'g\'ri so\'rov jo\'natoldi!',
            'errors': serializer.errors
        }
        return Response(res, status=400)

class TarifRetrieveUpdateDeleteAPIView(APIView):
    def get(self, request, pk):
        tarif = Tarif.objects.get(pk=pk)
        serializer = TarifSerializer(tarif)
        return Response(serializer.data)
    def put(self, request, pk):
        tarif = Tarif.objects.get(pk=pk)
        serializer = TarifSerializer(tarif, data=request.data)
        if serializer.is_valid():
            tarif.nom = serializer.validated_data['nom']
            tarif.narx = serializer.validated_data['narx']
            tarif.izoh = serializer.validated_data['izoh']
            tarif.davomiylik = serializer.validated_data['davomiylik']
            tarif.save()
            res = {
                'success': True,
                'massage': 'Ta\'rif muvaffaqiyatli o\'zgartirildi!',
                'data': serializer.data
            }
            return Response(res, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        tarif = Tarif.objects.get(pk=pk)
        tarif.delete()
        return Response({"success": True, "massage": "Ta\'rif o'chirildi!"}, status=204)

class KinoAPIView(APIView):
    def get(self, request):
        kinolar = Kino.objects.all()
        serializer = KinoSerializer(kinolar, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer =KinoPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

