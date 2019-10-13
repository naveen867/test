from App.models import WordFrequency
from rest_framework import serializers

class WordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WordFrequency
        fields = ['word', 'frequency']

    def update(self, instance, validated_data):
        instance.word = validated_data.get("word", instance.word)
        instance.frequency = validated_data.get("frequency", instance.frequency)
        instance.save()
        return instance

