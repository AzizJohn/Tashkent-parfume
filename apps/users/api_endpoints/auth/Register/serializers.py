from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.users.models import User
from apps.cart.models import Cart


class RegisterSerializer(ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["phone_number", "full_name", "password1", "password2"]

    def validate(self, attrs):
        phone_number = attrs.get("phone_number")
        full_name = attrs.get("full_name")
        password1 = attrs.get("password1")
        password2 = attrs.get("password2")

        if password1 != password2:
            raise serializers.ValidationError({"password": "Passwords must match."})

        user_qs = User.objects.filter(phone_number=phone_number)
        if user_qs.exists() and user_qs.is_deleted is False:
            raise serializers.ValidationError({"phone_number": "This phone number has already been registered."})

        # Sanitize full_name input by removing special characters
        sanitized_full_name = "".join(e for e in full_name if e.isalnum())
        if len(sanitized_full_name) < 4 or sanitized_full_name is None:
            raise serializers.ValidationError({"full_name": "Full name must be at least 5 characters long."})

        if len(password1) < 8:
            raise serializers.ValidationError({"password": "Password must be at least 8 characters long."})

        return attrs

    def create(self, validated_data):
        phone_number = validated_data.get("phone_number")
        full_name = validated_data.get("full_name")
        password = validated_data.get("password1")

        user_obj = User(phone_number=phone_number, full_name=full_name, is_deleted=False, is_active=True)
        user_obj.set_password(password)
        user_obj.save()
        # Cart.objects.create(user=user_obj, in_order=False)
        return user_obj
