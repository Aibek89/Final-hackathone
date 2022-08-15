from rest_framework import serializers

from post.models import Post, Comment, Image, Contact
from post.tasks import send_post_info

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')


    class Meta:
        model = Comment
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'



class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    comment = CommentSerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)


    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        requests = self.context.get('request')
        images = requests.FILES
        post = Post.objects.create(**validated_data)

        for image in images.getlist('images'):
            Image.objects.create(post=post, image=image)

        # send_post_info.delay(validated_data['name'])
        return post


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'



