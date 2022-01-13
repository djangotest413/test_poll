from rest_framework import serializers
from test_app.models import Polls, Questions, Answers


class PollsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polls
        fields = ['name', 'end_time', 'description', ]


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['poll', 'question_text', 'type']

class PollsListSerializer(serializers.ModelSerializer):
    questions = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='question_text'
    )
    class Meta:
        model = Polls
        fields = ['name', 'end_time', 'description', 'questions']


class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ['user_id', 'poll', 'question', 'answer']
