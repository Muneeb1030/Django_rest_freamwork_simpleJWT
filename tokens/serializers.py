from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    # first_name = serializers.CharField(max_length=30, required=False, allow_blank=True)
    # last_name = serializers.CharField(max_length=30, required=False, allow_blank=True)
    date_joined = serializers.DateTimeField(read_only=True)