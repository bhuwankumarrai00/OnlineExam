from django.urls import path
from .views import *

urlpatterns = [
    path('new-question/',newQuestion),
    path('save-question/',saveQuestion),
    path('view-questions/',viewQuestions),
    path('edit-question/',editQuestion),
    path('edit-save-question/',editSaveQuestion),
    path('delete-question/',deleteQuestion),
    path('signup/',signup),
    path('save-user/',saveUser),
    path('login/',login),
    path('login-validation/',loginValidation),
    path('logout/',logout),
    path('home/',home),
    path('start-test/',startTest),
    path('test-result/',testResult),

]
