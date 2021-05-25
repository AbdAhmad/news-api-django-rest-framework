from rest_framework import serializers
from news_app.models import Article

class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    author = serializers.CharField()
    body = serializers.CharField()
    publication_date = serializers.DateField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Article.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.author)    
        instance.title = validated_data.get('title', instance.title)  
        instance.body = validated_data.get('body', instance.body)  
        instance.publication_date = validated_data.get('publication_date', instance.publication_date)  
        instance.active = validated_data.get('active', instance.active) 
        instance.save()
        return instance