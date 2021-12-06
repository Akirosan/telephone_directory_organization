from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response

from .models import Company, Staffer
from .permissions import IsCreatorOrReadOnly, IsManagerOrReadOnly
from .serializers import (CompanySerializer, ManagerSerializer,
                          StafferSerializer)

User = get_user_model()


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(
        methods=['get'],
        detail=False,
        url_path='my',
        permission_classes=[IsAuthenticated],
    )
    def get_my_company(self, request):
        queryset = self.queryset.filter(creator=self.request.user)
        serializer = CompanySerializer(queryset, many=True)
        return Response(serializer.data)


class StafferViewSet(viewsets.ModelViewSet):
    permission_classes = [IsCreatorOrReadOnly | IsManagerOrReadOnly]
    queryset = Staffer.objects.all()
    serializer_class = StafferSerializer
    pagination_class = PageNumberPagination


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ManagerSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsCreatorOrReadOnly]

    def filter_queryset(self, queryset):
        queryset = self.queryset.filter(
            myorganisations__manager=self.request.user
        )
        return queryset

    @action(
        methods=['delete'],
        detail=False,
        permission_classes=[IsCreatorOrReadOnly],
    )
    def delete(self, request):
        company = get_object_or_404(
            Company, id=request.data.get('company')
            )
        company.manager.remove(
            get_object_or_404(User, email=request.data.get('email'))
        )
        return Response({"Удален"},)
