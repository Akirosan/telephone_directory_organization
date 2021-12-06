from rest_framework.generics import get_object_or_404
from rest_framework.permissions import SAFE_METHODS, BasePermission

from .models import Company


class IsManagerOrReadOnly(BasePermission):
    message = 'Вы не являетесь управляющим организации.'

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        mycompany = get_object_or_404(Company, id=request.data.get('company'))
        if mycompany.manager == request.user: # IN DEVELOP
            return True
        return False


class IsCreatorOrReadOnly(BasePermission):
    message = 'Вы не являетесь создателем организации.'

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        mycompany = get_object_or_404(Company, id=request.data.get('company'))
        if mycompany.creator == request.user:
            return True
        return False
