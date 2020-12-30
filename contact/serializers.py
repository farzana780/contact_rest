from rest_framework import serializers
from .models import Contact_data, Email, Phone

class EmailSerializers(serializers.ModelSerializer):
    employee = serializers.CharField(source='employee.name', read_only=True)
    class Meta:
        model = Email
        fields = ['employee', 'email']

    # def to_representation(self, instance):
    #     self.fields['employee'] = UserSerializer(read_only=True)
    #     return super(EmailSerializers, self).to_representation(instance)

class PhoneSerializers(serializers.ModelSerializer):
    employee = serializers.CharField(source='employee.name', read_only=True)
    class Meta:
        model = Phone
        fields = ['employee', 'phone']

    # def to_representation(self, instance):
    #     self.fields['employee'] = UserSerializer(read_only=True)
    #     return super(PhoneSerializers, self).to_representation(instance)


class UserSerializer(serializers.ModelSerializer):
    email = serializers.StringRelatedField(many=True, read_only=True)
    phone = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Contact_data
        fields = ['id', 'name', 'email', 'phone']



class ContactSerializer(serializers.ModelSerializer):
   email = EmailSerializers(many=True)
   phone = PhoneSerializers(many=True)

   class Meta:
       model = Contact_data
       fields = "__all__"

   def create(self, validated_data):
       email_data = validated_data.pop('email')
       phone_data = validated_data.pop('phone')
       employee = Contact_data.objects.create(**validated_data)
       for data in email_data:
           data['employee'] = employee
           Email.objects.create(**data)
       for data in phone_data:
           data['employee'] = employee
           Phone.objects.create(**data)
       return employee
