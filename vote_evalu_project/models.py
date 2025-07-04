from django.db import models

# 프로젝트 모델
class Project(models.Model):
    title = models.CharField(max_length=100)       # 제목 필드 (최대 100자)
    description = models.TextField()               # 설명 필드 (글자 수 제한 없음)

    def __str__(self):
        return self.title                          # 관리자 화면에 제목 보이게 설정
