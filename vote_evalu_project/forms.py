from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']



# 1~5점 중 하나를 선택할 수 있는 평가 폼
class EvaluationForm(forms.Form):
    score = forms.ChoiceField(
        choices=[(i, f"{i}점") for i in range(1, 6)],  # 1~5점 선택지
        label="평가 점수",
        widget=forms.RadioSelect  
    )
