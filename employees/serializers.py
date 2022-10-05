from rest_framework import serializers
from .models import Employee, Cloth

from users.serializers import EnterpriseSerializer


class ClothSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cloth
        exclude = ['empregado']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    empresa = serializers.IntegerField(source='empresa.id', required=False)
    roupas = ClothSerializer(many=True)

    def create(self, validated_data):
        nome = validated_data.get('nome')
        empresa = validated_data.get('empresa')
        roupas = map(dict, validated_data.get('roupas'))

        empregado = self.Meta.model.objects.create(nome=nome, empresa=empresa)

        for r in roupas:
            roupa = ClothSerializer(data={ **r, "empregado": empregado })
            roupa.is_valid(raise_exception=True)
            roupa.create({ **r, "empregado": empregado })

        return empregado

    def update(self, instance, validated_data):
        nome = validated_data.get('nome', instance.nome)
        roupas = map(dict, validated_data.get('roupas', instance.roupas))

        instance.nome = nome

        for r in roupas:
            Cloth.objects.update_or_create(
                empregado=instance,
                tipo=r.get("tipo"),
                defaults={
                    **r,
                }
            )

        instance.save()
        return instance




class EmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    empresa = serializers.IntegerField(source='empresa.id', required=False)
