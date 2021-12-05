from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Company, Staffer
from .permissions import IsCreatorManagerOrRedonly
from .serializers import (CompanySerializer, ManagerSerializer,
                          StafferSerializer)

User = get_user_model()


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]

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
    queryset = Staffer.objects.all()
    serializer_class = StafferSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsCreatorManagerOrRedonly]


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ManagerSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsCreatorManagerOrRedonly, ]

    def filter_queryset(self, queryset):
        queryset = self.queryset.filter(
            myorganisations__manager=self.request.user
        )
        return queryset

