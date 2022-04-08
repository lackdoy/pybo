from cProfile import label
from dataclasses import field
from msilib.schema import Class
from tkinter import Widget
from django import forms
from pybo.models import Question, Answer, Comment

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        labels = {
            'subject' : '제목',
            'content' : '내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        lables = {
            'content' : '답변내용',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {'content':'댓글내용',}