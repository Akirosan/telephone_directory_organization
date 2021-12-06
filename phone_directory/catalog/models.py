from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='thecompany',
        verbose_name='Создатель',
    )
    manager = models.ManyToManyField(
        User,
        related_name='myorganisations',
        verbose_name='Управляющий',
        blank=True
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Название',
        unique=True,
    )
    adress = models.CharField(
        max_length=100,
        verbose_name='Адрес'
    )
    description = models.TextField(
        max_length=200,
        verbose_name='Описание компании'
    )
    created = models.DateField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
        ordering = ['name']

    def __str__(self):
        return self.name


class Staffer(models.Model):
    staffer = models.CharField(
        max_length=100,
        verbose_name='ФИО'
    )
    post = models.CharField(
        max_length=100,
        verbose_name='Должность'
    )
    work_phone = models.CharField(
        blank=True,
        max_length=12,
        verbose_name='Рабочий телефон'
    )
    personal_phone = models.CharField(
        blank=True,
        max_length=12,
        unique=True,
        verbose_name='Личный телефон'
    )
    fax_number = models.CharField(
        blank=True,
        max_length=12,
        verbose_name='Факс'
    )
    company = models.ManyToManyField(
        Company,
        related_name='staffers',
        verbose_name='Сотрудники'
    )

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['staffer']

    def __str__(self):
        return self.staffer
