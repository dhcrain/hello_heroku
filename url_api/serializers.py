from rest_framework import serializers
from short_app.models import Click


class ClickSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Click
        fields = ['link', 'time_click']
