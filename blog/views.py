from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView , DetailView , View

from .forms import CommentForm

from .models import Post

# Create your views here. reteutn objecy list 
class StPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering =["-date"]
    # we need context object name to change a name of return data like in line 25-26 
    context_object_name = "posts"

    def get_queryset(self):
        queryset= super().get_queryset()
        data = queryset[:3]
        return data



# def starting_page(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3]
#     return render(request, "blog/index.html", {
#       "posts": latest_posts
#     })

################ ALLLL POSTS by using VIREWS KIST 
    
# def posts(request):
#     all_posts = Post.objects.all().order_by("-date")
#     return render(request, "blog/all-posts.html", {
#       "all_posts": all_posts
#     })
    
class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"


       
# Detail view 
    


# def post_detail(request, slug):
#     identified_post = get_object_or_404(Post, slug=slug)
#     return render(request, "blog/post-detail.html", {
#       "post": identified_post,
#       "post_tags": identified_post.tags.all()
#     })
    
class SinglePostView(View):
    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
          is_saved_for_later = post_id in stored_posts
        else:
          is_saved_for_later = False

        return is_saved_for_later

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            # here we have cretaed a form for single post view  and pass it in html 
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "blog/post-detail.html", context)
   
        


