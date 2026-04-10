from rest_framework import serializers
from .models import Realisation, RealisationImage


class RealisationImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = RealisationImage
        fields = ['id', 'image']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None


class RealisationSerializer(serializers.ModelSerializer):
    images = RealisationImageSerializer(many=True, read_only=True)

    class Meta:
        model = Realisation
        fields = '__all__'