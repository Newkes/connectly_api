from rest_framework import serializers
from django.contrib.auth.models import User
from .models import  Post, Comment


class UserSerializer(serializers.ModelSerializer):
    
    date_created = serializers.DateTimeField(source='date_joined', read_only=True)
    
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_created', 'password']

   # def create(self, validated_data):
        # This follows Step 2 of your instructions: Use create_user for hashing
        #return User.objects.create_user(
        #    username=validated_data['username'],
        #    email=validated_data.get('email', ''),
        #    password=validated_data['password']
        #)


class PostSerializer(serializers.ModelSerializer):
    comments = serializers.StringRelatedField(many=True, read_only=True)


    class Meta:
        model = Post
        fields = ['id', 'content', 'author', 'date_created', 'comments']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'author', 'post', 'date_created']


    def validate_post(self, value):
        if not Post.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Post not found.")
        return value


    def validate_author(self, value):
        if not User.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Author not found.")
        return value



