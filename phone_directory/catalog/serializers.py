from collections import OrderedDict

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers, status
from rest_framework.response import Response

from .models import Company, Staffer


class StafferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staffer
        fields = (
            'staffer',
            'post',
            'work_phone',
            'personal_phone',
            'fax_number',
            'company'
        )

    def to_representation(self, instance):
        result = super(StafferSerializer, self).to_representation(instance)
        return OrderedDict(
            [(key, result[key]) for key in result if result[key]]
        )

    def validate(self, attrs):
        if (
            attrs.get('work_phone') is None
            and attrs.get('personal_phone') is None
            and attrs.get('work_phone') is None
        ):
            raise ValueError('Должен быть хотя бы один номер телефона')
        return super().validate(attrs)


class CompanySerializer(serializers.ModelSerializer):
    staffer = StafferSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ('name', 'adress', 'description', 'staffer')

    def create(self, validated_data):
        creator = self.context['request'].user
        company = Company.objects.create(
            creator=creator, **validated_data
        )
        return company


class ManagerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('username', 'email')

    def create(self, validated_data):
        company = get_object_or_404(
            Company, id=self.initial_data.get('company')
            )
        company.manager.add(
            get_object_or_404(User, email=self.initial_data.get('email'))
        )
        return Response({"Добавлен"}, status=status.HTTP_201_CREATED,)


class CustomUserSerializer(UserCreateSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        )
