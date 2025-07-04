from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProjectForm, EvaluationForm  # 평가 폼 가져오기
from .models import Project, Evaluation         # 평가 모델 가져오기
from django.db.models import Avg

# 프로젝트 시작 페이지 설정
def home(request):
    return render(request, 'vote_evalu_project/home.html')

# 프로젝트 생성 페이지 처리
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_success')
    else:
        form = ProjectForm()
    return render(request, 'vote_evalu_project/create_project.html', {'form': form})

# 프로젝트 생성 완료 페이지
def project_success(request):
    return render(request, 'vote_evalu_project/project_success.html')

# 프로젝트 리스트 페이지( 평균 점수 기준 높은순 정렬 )
def project_list(request):
    projects = Project.objects.annotate(avg_score=Avg('evaluations__value')).order_by('-avg_score')
    return render(request, 'vote_evalu_project/project_list.html', {'projects': projects})

# 프로젝트 상세 페이지 + 평가 폼 + 평균 점수 계산 + 제출 결과 확인
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)

    # 세션에서 방금 투표한 점수를 꺼냄 (한 번만 사용되게 pop)
    user_score = request.session.pop('user_score', None)
    voted = bool(user_score)  # 투표 완료 여부

    if request.method == 'POST':
        form = EvaluationForm(request.POST)
        if form.is_valid():
            score = int(form.cleaned_data['score'])
            Evaluation.objects.create(project=project, value=score)
            request.session['user_score'] = score  # 세션에 저장
            return redirect('project_detail', pk=pk)  # 리다이렉트로 폼 초기화
    else:
        form = EvaluationForm()  # 항상 비어있는 폼

    evaluations = project.evaluations.all()
    score_list = [e.value for e in evaluations]
    average = round(sum(score_list) / len(score_list), 2) if score_list else None

    return render(request, 'vote_evalu_project/project_detail.html', {
        'project': project,
        'form': form,
        'average': average,
        'score_list': score_list,
        'user_score': user_score,
        'voted': voted,
    })

# 프로젝트별 평균 점수를 계산하고 평균 내림차순 정렬
def sorted_project_list(request):
    projects = Project.objects.annotate(avg_score=Avg('evaluations__value')).order_by('-avg_score')
    return render(request, 'vote_evalu_project/sorted_project_list.html', {'projects': projects})