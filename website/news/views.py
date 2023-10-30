from typing import Any, Dict
from django.views import generic
from .models import Post, FeedBack, Documents, Activities, Anti_corrupsion, Plans, Examinations
from .forms import CreateFeedBackForm, SearchForm
from django.db.models import Q
from .utils import get_client_ip, send_contact_email_message
from django.http import JsonResponse
from django.template.loader import render_to_string

from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.views.generic import CreateView
from website import settings

from django.http import FileResponse, Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View

def exams_material(request):
    materials = Examinations.objects.order_by('-created_at')
    context = {
        'documents' : materials
    }
    return render(request, 'examinations.html', context)

class ExaminationsViewList(View):
    def get(self, request, **kwargs):
        anti_corruption = get_object_or_404(Examinations, id=kwargs['exam_id'])
        if not anti_corruption.document:  # if document file is not found
            raise Http404
        # return the document file as a response
        response = FileResponse(anti_corruption.document)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        anti_coruption = get_object_or_404(Activities, id=self.kwargs['exam_id'])
        context['exam_id'] = anti_coruption.id  # pass document_id to context dictionary
        return context

def plans_material(request):
    materials = Plans.objects.order_by('-created_at')
    context = {
        'documents' : materials
    }
    return render(request, 'plans_about.html', context)

class PlansViewList(View):
    def get(self, request, **kwargs):
        anti_corruption = get_object_or_404(Plans, id=kwargs['plans_id'])
        if not anti_corruption.document:  # if document file is not found
            raise Http404
        # return the document file as a response
        response = FileResponse(anti_corruption.document)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        anti_coruption = get_object_or_404(Activities, id=self.kwargs['plans_id'])
        context['plans_id'] = anti_coruption.id  # pass document_id to context dictionary
        return context

def anti_corruption_materials(request):
    materials = Anti_corrupsion.objects.filter(status=1).order_by('-created_at')
    context = {
        'documents' : materials
    }
    return render(request, 'teaching_materials.html', context)

def anti_corruption_expertise(request):
    return render(request, 'expertise.html')

class AntiCorruptionViewList(View):
    def get(self, request, **kwargs):
        anti_corruption = get_object_or_404(Anti_corrupsion, id=kwargs['plans_id'])
        if not anti_corruption.document:  # if document file is not found
            raise Http404
        # return the document file as a response
        response = FileResponse(anti_corruption.document)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        anti_coruption = get_object_or_404(Activities, id=self.kwargs['plans_id'])
        context['plans_id'] = anti_coruption.id  # pass document_id to context dictionary
        return context

def activities_audit_main_list(request):
    audit_activities = Activities.objects.filter(status=10).order_by('-created_at')
    context = {
        'documents' : audit_activities
    }
    return render(request, 'audit.html', context)

def activities_publications_main_list(request):
    publications_activities = Activities.objects.filter(status=9).order_by('-created_at')
    context = {
        'documents' : publications_activities
    }
    return render(request, 'publications.html', context)

def activities_plans_main_list(request):
    plans_activities = Activities.objects.filter(status=8).order_by('-created_at')
    context = {
        'documents' : plans_activities
    }
    return render(request, 'plan.html', context)

def activities_solutions_main_list(request):
    solutions_activities = Activities.objects.filter(status=7).order_by('-created_at')
    context = {
        'documents' : solutions_activities
    }
    return render(request, 'solutions.html', context)

def activities_events_main_list(request):
    events_activities = Activities.objects.filter(status=6).order_by('-created_at')
    context = {
        'documents' : events_activities
    }
    return render(request, 'events.html', context)

def activities_statements_main_list(request):
    statements_activities = Activities.objects.filter(status=5).order_by('-created_at')
    context = {
        'documents' : statements_activities
    }
    return render(request, 'statements.html', context)

def activities_info_main_list(request):
    info_actvities = Activities.objects.filter(status=4).order_by('-created_at')
    context = {
        'documents' : info_actvities
    }
    return render(request, 'info.html', context)

def activities_college_main_list(request):
    college_activities = Activities.objects.filter(status=3).order_by('-created_at')
    context = {
        'documents' : college_activities
    }
    return render(request, 'college.html', context)

def activities_analitycal_main_list(request):
    analytical_activities = Activities.objects.filter(status=2).order_by('-created_at')
    context = {
        'documents' : analytical_activities
    }

    return render(request, 'analitycal.html', context)

def activities_control_main_list(request):
    control_activities = Activities.objects.filter(status=1).order_by('-created_at')
    context = {
        'documents' : control_activities
    }

    return render(request, 'control.html', context)

class ActivitiesViewList(View):
    def get(self, request, **kwargs):
        activities = get_object_or_404(Activities, id=kwargs['activities_id'])
        if not activities.document:  # if document file is not found
            raise Http404
        # return the document file as a response
        response = FileResponse(activities.document)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        activities = get_object_or_404(Activities, id=self.kwargs['activities_id'])
        context['activities_id'] = activities.id  # pass document_id to context dictionary
        return context

def activities_report_main_list(request):
    work_plan = Activities.objects.filter(status=0).order_by('-created_at')
    context = {
        'documents' : work_plan
    }
    return render(request, 'report.html', context)

class ReportView(generic.TemplateView):
    template_name = 'report.html'

class ActivitiesView(generic.TemplateView):
    template_name='activities.html'

def regular_document_list(request):
    documents=Documents.objects.filter(status=3).order_by('-created_at')

    paginator = Paginator(documents, 10)
    page = request.GET.get('page')
    docs = paginator.get_page(page)

    context = {
        'docs' : docs
    }

    return render(request, 'regular_legal_acts.html', context)

class StuffingView(generic.TemplateView):
    template_name='Staffing.html'

class ProcuromentView(generic.TemplateView):
    template_name='procuroment.html'

class SynopsisView(generic.TemplateView):
    template_name='synopsis.html'

class StructureView(generic.TemplateView):
    template_name='structure.html'

class IfsView(generic.TemplateView):
    template_name = 'ifs.html'

class InformationView(generic.TemplateView):
    template_name = 'information.html'

class MangmentView(generic.TemplateView):
    template_name = 'managment.html'

class TasksView(generic.TemplateView):
    template_name = 'tasks.html'

class DocumentViewList(View):
    def get(self, request, **kwargs):
        document = get_object_or_404(Documents, id=kwargs['document_id'])
        if not document.document:  # if document file is not found
            raise Http404
        # return the document file as a response
        response = FileResponse(document.document)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        document = get_object_or_404(Documents, id=self.kwargs['document_id'])
        context['document_id'] = document.id  # pass document_id to context dictionary
        return context

def documents_main_list(request):
    documents = Documents.objects.filter(status=0).order_by('-created_at')
    documents_SFK = Documents.objects.filter(status=1).order_by('-created_at')
    documents_Metod = Documents.objects.filter(status=2).order_by('-created_at')
    context = {
        'documents' : documents,
        'documents_SFK' : documents_SFK,
        'documents_metod' : documents_Metod
    }
    return render(request, 'main_documents.html', context)

def search(request):
    query = request.GET.get('q')
    search_results = []

    # Ищем посты, содержащие запрос
    posts = Post.objects.filter(title__icontains=query) | Post.objects.filter(content__icontains=query)
    documents = Documents.objects.filter(title__icontains=query)
    activities = Activities.objects.filter(title__icontains=query)
    anti_corrupsion = Anti_corrupsion.objects.filter(title__icontains=query)
    feedbacks = FeedBack.objects.filter(subject__icontains=query) | FeedBack.objects.filter(content__icontains=query)

    # Ищем документы, содержащие запрос

    # Объединяем результаты поиска
    search_results.extend(posts)
    search_results.extend(documents)
    search_results.extend(activities)
    search_results.extend(anti_corrupsion)
    search_results.extend(feedbacks)

    # Создаем объект Paginator для пагинации результатов поиска
    paginator = Paginator(search_results, 10)

    # Получаем номер страницы из GET-параметра
    page_number = request.GET.get('page')

    # Получаем объекты для текущей страницы
    page_obj = paginator.get_page(page_number)

    # Отображаем шаблон с результатами поиска
    return render(request, 'search_result_list.html', {'page_obj': page_obj, 'query': query})

class Connection(generic.TemplateView):
    template_name = 'connection.html'

def function_based(request):
    posts = Post.objects.filter(status=1)
    paginator = Paginator(posts, 12)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    return render(request, 'all_news.html', {'posts':posts})


class PostList(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self):
        context = super().get_context_data()

        latest_post = Post.objects.latest('created_on')
        context['latest_post'] = latest_post

        posts_before_latest = Post.objects.all().exclude(pk=latest_post.pk)[:3]
        context['posts_before_latest'] = posts_before_latest

        posts_5_to_10 = Post.objects.all()[4:7]
        context['posts_5_to_10'] = posts_5_to_10

        return context

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class DocumentView(generic.TemplateView):
    template_name = 'documents.html'

    def get_context_data(self):
        context = super().get_context_data()

        documents = Documents.objects.all()
        context['documents'] = documents

        return context

class AboutView(generic.TemplateView):
    template_name = 'about.html'


class AntiCorruption(generic.TemplateView):
    template_name = 'anti-corruption.html'

    def get_context_data(self):
        context=super().get_context_data()

        anti_corrupsion = Anti_corrupsion.objects.filter(status=0).order_by('-created_at')
        context['documents'] = anti_corrupsion

        return context

class FeedbackCreateView(SuccessMessageMixin, CreateView):
    model = FeedBack
    form_class = CreateFeedBackForm
    success_message = "Пришло письмо!"
    template_name = 'feedback.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контактная информация'
        return context
    
    def form_valid(self, form):

        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.ip_address = get_client_ip(self.request)
            user_id = getattr(feedback, 'user_id', None)
            send_contact_email_message(feedback.subject, feedback.email, feedback.content, feedback.ip_address, user_id)
        
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('home')
    
    def get_feedback_list(self):
        return self.model.objects.all()

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        feedback_list = self.model.objects.all()[:5]
        context = {'form': form, 'feedback_list': feedback_list, 'recaptcha_site_key': settings.RECAPTCHA_PUBLIC_KEY}
        return render(request, self.template_name, context)

class FeedbackListView(View):
    def get(self, request):
        start = int(request.GET.get('start', 0))
        feedback_list = FeedBack.objects.all()[start:start+5]
        feedback_data = [{'subject': feedback.subject, 'content': feedback.content, 'email': feedback.email, 'created_at': feedback.created_at, 'answer': feedback.answer} for feedback in feedback_list]
        return JsonResponse({'feedback_list': feedback_data})

class HtmlVIewer(generic.TemplateView):
    template_name = '1.html'
    