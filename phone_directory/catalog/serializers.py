from collections import OrderedDict

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from .models import Company, Staffer


class StafferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staffer
        fields = '__all__'

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
        staffers = self.initial_data.get('staffer')
        for staff in staffers:
            company.staffer.add(get_object_or_404(Staffer, pk=staff))
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
        if company.creator == self.context['request'].user:
            company.manager.add(
                get_object_or_404(User, email=self.initial_data.get('email'))
            )
            return company
        else:
            raise ValueError('Вы не являетесь создателем этой компании')
