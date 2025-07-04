from django.db import models

# 프로젝트 모델
class Project(models.Model):
    title = models.CharField(max_length=100)       # 제목 필드 (최대 100자)
    description = models.TextField()               # 설명 필드 (글자 수 제한 없음)

    def __str__(self):
        return self.title                          # 관리자 화면에 제목 보이게 설정
    
# 평가(점수) 모델 
class Evaluation(models.Model):
    project = models.ForeignKey(Project, related_name='evaluations', on_delete=models.CASCADE)
    value = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    def __str__(self):
        return f'{self.project.title} - {self.value}점'

