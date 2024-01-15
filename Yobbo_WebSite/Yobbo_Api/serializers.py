from rest_framework import serializers
from .models import YobboAdmin, Post

class YobboAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = YobboAdmin
        fields = ['id','name','email','password']
        extra_kwargs = {
            'password': {'write_only':True}
        }
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
    
    