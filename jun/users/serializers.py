from rest_framework.relations import HyperlinkedIdentityField, HyperlinkedRelatedField
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from models import User


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

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



