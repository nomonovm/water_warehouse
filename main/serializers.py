from rest_framework import serializers
from .models import Suv, Mijoz, Sotuvchi, Haydovchi, Buyurtma


class SuvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suv
        fields = '__all__'

    def validate_litr(self, value):
        if value > 19:
            raise serializers.ValidationError("Bunday katta litrlarda suv sotilmaydi")
        return value


class MijozSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mijoz
        fields = '__all__'


class SotuvchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sotuvchi
        fields = ['id', 'username', 'yosh', 'ish_vaqti']

    def validate_yosh(self, value):
        if value < 19:
            raise serializers.ValidationError("Yoshingiz mos kelmaydi")
        return value


class HaydovchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Haydovchi
        fields = '__all__'


class BuyurtmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = '__all__'

    def validate(self, data):
        mijoz = data['mijoz']
        if mijoz.qarz > 500000:
            raise serializers.ValidationError("Qarzingiz juda ko‘p, buyurtma qilolmaysiz!")
        return data
