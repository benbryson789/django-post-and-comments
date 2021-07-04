from django.shortcuts import render,redirect
from .models import Posts,Comments
#posts list
def posts_list(request):
    posts = Posts.objects.all()
    return render(request,'posts.html',{'data':posts})
# post detail.
def posts_details(request,id):
    post = Posts.objects.filter(id=id).first()
    comments = Comments.objects.filter(post_id=id).all()
    if request.method  == 'POST':
        obj = Comments()
        obj.name =request.POST['name']
        obj.email =request.POST['email']
        obj.comment_title =request.POST['title']
        obj.comment_content =request.POST['content']
        obj.post_id =request.POST['post_id']
        obj.save()
        return redirect("/details/"+request.POST['post_id'])
    return render(request,'post-details.html',{'post':post,'comments':comments})
# add new post.
def add_post(request):
    if request.method == 'POST':
        obj = Posts()
        obj.content = request.POST['content']
        obj.title = request.POST['title']
        obj.save()
        return redirect('/')
    return render(request,'add-post.html') 