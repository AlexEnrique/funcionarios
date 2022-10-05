from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Cloth, Employee
from .serializers import EmployeeSerializer, EmployeeListSerializer, ClothSerializer
from .permissions import IsOwner


class EmployeeViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def list(self, request, *args, **kwargs):
        list = Employee.objects.filter(empresa__user=request.auth.user)
        return Response(EmployeeListSerializer(list, many=True).data)

    def retrieve(self, request, *args, pk=None, **kwargs):
        obj = get_object_or_404(Employee, pk=pk)
        self.check_object_permissions(request, obj)
        return Response(EmployeeSerializer(obj).data)

    def create(self, request, *args, **kwargs):
        serializer: EmployeeSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        obj = serializer.create({
            **serializer.data,
            "empresa": request.auth.user.enterprise,
        })

        # obj = Employee.objects.create(
        #     nome=serializer.data["nome"],
        #     empresa=request.auth.user.enterprise,
        # )

        return Response(EmployeeSerializer(obj).data, status=201)

    def update(self, request, *args, pk=None,  **kwargs):
        obj = get_object_or_404(Employee, pk=pk)
        self.check_object_permissions(request, obj)

        serializer = EmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        print(serializer.data)

        obj = serializer.update(obj, serializer.data)

        return Response(EmployeeSerializer(obj).data)

    def destroy(self, request, *args, pk=None, **kwargs):
        obj = get_object_or_404(Employee, pk=pk)
        self.check_object_permissions(request, obj)
        obj.delete()
        return Response(status=204)

    @action(["PATCH"], detail=True, url_path="salvar-preferencias")
    def save_preference(self, request, pk=None, **kwargs):
        obj = get_object_or_404(Employee, pk=pk)
        self.check_object_permissions(request, obj)

        serializer = ClothSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        Cloth.objects.update_or_create(
            empregado=obj,
            tipo=serializer.data["tipo"],
            defaults={
                "tamanho": serializer.data["tamanho"],
                "cor": serializer.data["cor"],
            }
        )

        return Response(EmployeeSerializer(obj).data)
