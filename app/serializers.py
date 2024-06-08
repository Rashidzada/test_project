from rest_framework import serializers

from .models import Contact
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id','name', 'email', 'subject', 'message']
        # read_only_fields = ['name', 'email', 'subject', 'message']
        # extra_kwargs = {
        #     'name': {'required': True},
        #     'email': {'required': True},
        #     'subject': {'required': True},
        #     'message': {'required': True},}
        # def create(self, validated_data):
        #     return Contact.objects.create(**validated_data)
        # def update(self, instance, validated_data):
        #     instance.name = validated_data.get('name', instance.name)
        #     instance.email = validated_data.get('email', instance.email)
        #     instance.subject = validated_data.get('subject', instance.subject)
        #     instance.message = validated_data.get('message', instance.message)
        #     instance.save()
        #     return instance