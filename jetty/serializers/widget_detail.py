from rest_framework import serializers

from jetty.models.widget import Widget


class WidgetDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Widget
        fields = (
            'id',
            'widget_type',
            'name',
            'x',
            'y',
            'width',
            'height',
            'params',
            'date_add',
            'dashboard'
        )