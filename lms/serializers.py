from rest_framework import serializers
from lms.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    """ Сериализатор урока """

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    """ Сериализатор курса """

    # Добавляем поле с числом уроков в курсе
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self, instance):
        return instance.lessons.count()
