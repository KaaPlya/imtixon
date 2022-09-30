from pyexpat import model
from rest_framework.serializers import ModelSerializer
from .models import News


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"

    def to_representation(self, instance):

        if instance.name == "0":
            name = "Nol edi"
        else:
            name = instance.name

        return {
            "id": instance.id,
            "name": name,
            "text": instance.text,
            "category": instance.category.name,
            "created_at": instance.created_at,
            "updated_at": instance.updated_at,
        }