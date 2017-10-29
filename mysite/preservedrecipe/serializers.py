from rest_framework import serializers
from .models import IngredientMaster, Classification


class ClassificationSerializer(serializers.HyperlinkedModelSerializer):
    #classification = serializers.StringRelatedField(many=True)
    classification = serializers.PrimaryKeyRelatedField( queryset=Classification.objects.all())

    class Meta:
        model = Classification
        fields = ('classification_text', 'classification' )


class IngredientMasterSerializer(serializers.HyperlinkedModelSerializer):
    classification = serializers.PrimaryKeyRelatedField( queryset=Classification.objects.all())

    class Meta:
        model = IngredientMaster
        fields = ('name', 'text', 'classification')



