from test_app.models import Polls, Questions, Answers
from test_app.serializers import (
    PollsSerializer,
    QuestionsSerializer,
    PollsListSerializer,
    AnswersSerializer
)
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from django.utils.timezone import now
from django.shortcuts import get_object_or_404


class PollsCreateView(generics.CreateAPIView):
    #permission_classes = [IsAdminUser]
    queryset = Polls.objects.all()
    serializer_class = PollsSerializer


class PollsUpdateDeleteView(generics.UpdateAPIView, generics.DestroyAPIView):
    #permission_classes = [IsAdminUser]
    queryset = Polls.objects.all()
    serializer_class = PollsSerializer


class QuestionAddView(generics.CreateAPIView):
    #permission_classes = [IsAdminUser]
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer


class QuestionUpdateDeleteView(generics.UpdateAPIView, generics.DestroyAPIView):
    #permission_classes = [IsAdminUser]
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

class PollsListView(generics.ListAPIView):
    queryset = Polls.objects.filter(end_time__gt=(now()))
    serializer_class = PollsListSerializer


class QuestionsListView(generics.ListAPIView):
    serializer_class = QuestionsSerializer

    def get_queryset(self):
        questions = get_object_or_404(Polls, pk=self.kwargs['pk'])
        return questions.questions.all()


class AnswerAddView(generics.CreateAPIView):
    serializer_class = AnswersSerializer
    queryset = Answers.objects.all()


class AnswersListView(generics.ListAPIView):
    serializer_class = AnswersSerializer
    
    def get_queryset(self):
        return Answers.objects.filter(user_id=self.kwargs['user_id'])


    
    