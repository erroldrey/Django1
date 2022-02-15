from rest_framework.relations import HyperlinkedIdentityField, HyperlinkedRelatedField
from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import User
from .serializers import UserSerializer
from .models import Project


class ProjectSerializer(ModelSerializer):
    owner = HyperlinkedIdentityField(view_name='user-detail')

    users = HyperlinkedRelatedField(many=True, view_name='user-detail', read_only=True)

    class Meta:
        model = Project
        fields = '__all__'


class ProjectReadSerializer(ModelSerializer):
    owner = HyperlinkedIdentityField(view_name='user-detail')

    users = HyperlinkedRelatedField(many=True, view_name='user-detail', read_only=True)
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'

from rest_framework import mixins, viewsets
from .serializers import UserSerializer
from .models import User


class UserViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()




