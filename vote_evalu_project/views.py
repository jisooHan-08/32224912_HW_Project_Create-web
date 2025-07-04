from django.shortcuts import render, redirect
from .forms import ProjectForm  # 🔹 이 줄 추가

# 프로젝트 생성 페이지 처리
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_success')
    else:
        form = ProjectForm()
    return render(request, 'vote_evalu_project/create_project.html', {'form': form})  # 🔹 폼 넘김

# 프로젝트 생성 완료 페이지
def project_success(request):
    return render(request, 'vote_evalu_project/project_success.html')
