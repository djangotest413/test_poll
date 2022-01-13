from .views import (
    PollsCreateView,
    PollsUpdateDeleteView,
    QuestionAddView,
    QuestionUpdateDeleteView,
    PollsListView,
    QuestionsListView,
    AnswerAddView,
    AnswersListView,
)    
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('poll/', PollsCreateView.as_view()),
    path('poll/<int:pk>/', PollsUpdateDeleteView.as_view()),
    path('poll/question/', QuestionAddView.as_view()),
    path('poll/question/<int:pk>/', QuestionUpdateDeleteView.as_view()),
    path('poll/active/', PollsListView.as_view()),
    path('questions/<int:pk>/', QuestionsListView.as_view()),
    path('answer/', AnswerAddView.as_view()),
    path('polls/<int:user_id>/', AnswersListView.as_view()),
]