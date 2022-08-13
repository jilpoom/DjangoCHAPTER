from rest_framework import serializers
from .models import Todo


# 전체 조회용 Serializer, id, 제목, 완료여부, 중요 여부가 필요
class TodoSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'complete', 'important')

# 상세 조회용 Serializer, 미리 정의된 모델 전체 데이터를 직렬화(ToJson)
class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'created', 'complete', 'important')


# 생성용 Serializer, 입력할 field는  제목, 상세 정보, 중요 여부

class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title', 'description', 'important')