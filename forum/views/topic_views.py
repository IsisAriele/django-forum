from django.views import View
from django.shortcuts import render, redirect
from forum.models import Topic, Comment
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from forum.forms.topic_form import TopicRegistrationForm


class TopicListView(View):
    @method_decorator(login_required)
    def get(self, request):
        # O query param da requisição serve para realizar o filtro.
        # Query param nesse caso é o "?my_topics=true" informado na URL.
        query_topic_by_user = request.GET.get("my_topics", False)

        if not query_topic_by_user:
            topics = Topic.objects.all().order_by("-created_at")
        else:
            topics = Topic.objects.filter(user=request.user).order_by("-created_at")

        context = {"topics": topics}
        return render(request, "forum/index.html", context)


class TopicRegistrationView(View):
    def get(self, request):
        context = {"form": TopicRegistrationForm()}
        return render(request, "forum/topic.html", context)
    
    def post(self, request):
        form = TopicRegistrationForm(request.POST)
        if form.is_valid():
            topic = Topic(
                title=form.data["title"],
                text=form.data["text"],
                user=request.user,
            )
            topic.save()

            return redirect("index")
        
        # Deu ruim
        return render(request, "forum/topic.html", {})
    
class TopicVisualizationView(View):
    def get(self, request, topic_id):
        topic = Topic.objects.get(id=topic_id)
        comments = Comment.objects.filter(topic=topic)
        return render(request, "forum/topic_visualization.html", {"topic": topic, "comments": comments})
