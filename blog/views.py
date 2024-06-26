from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Post
from .forms import CommentForm

# Create your views here.

class PostList(generic.ListView):
    queryset=Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6

def post_detail(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments=post.comments.all().order_by("-created_on")
    comment_count=post.commentsfilter(approved=True).count()

    if request.method == "POST":
        print("Received a POST request")
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request,messages.SUCCESS,
                'Comment submitted and awaiting approval'

        )

    comment_form=CommentForm()

    print("About to render template")

    return render(
      request,
      "blog/post_detail.html",
      {
        "post": post,
        "comments" : comments,
        "comment_count": comment_count,
        "comment_form":comment_form,
      },
    )


#class EventsList(generic.ListView):
    #model = Event
    #template_name = "index.html"
    #paginate_by = 12


#def event_detail(request, event_id):
    
    #queryset = Event.objects.all()
    #event = get_object_or_404(queryset, event_id=event_id)

    #return render(
        #request,
        #"events/event_detail.html",
        #{"event": event}
    #)