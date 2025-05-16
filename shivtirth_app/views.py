from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    special_packages = Special_Packages.objects.all().order_by('-date_created')
    blog = Post.objects.order_by('-date_created')[:3]

    context = {
        'special_packages': special_packages,
        'blog': blog,
    }

    return render(request, 'main/index.html', context)

def about(request):
    return render(request, 'main/about.html')

def packages(request):
    special_packages = Special_Packages.objects.all().order_by('-date_created')
    packages = Packages.objects.all().order_by('-date_created')

    context = {
        'special_packages': special_packages,
        'packages': packages,
    }

    return render(request, 'main/packages.html', context)

def gallery(request):
    gallery = Gallery.objects.all().order_by('-date_created')[:50]

    context = {
        'gallery': gallery
    }

    return render(request, 'main/gallery.html', context)

def blog(request):
    blog = Post.objects.order_by('-date_created')[:5]

    context = {
        'blog':blog,
    }

    return render(request, 'main/blog.html', context)

def blog_single(request, pk):
    detail = Post.objects.get(id=pk)
    blog = Post.objects.order_by('-date_created')[:4]

    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.blog = detail
            instance.name = request.user
            instance.save()
            return redirect ('detail', pk=detail.id)
    else:
        c_form = CommentForm()
    
    context = {
        'detail': detail,
        'blog': blog,
        'c_form': c_form,
    }

    return render(request, 'main/blog-single.html', context)

def contact(request):
    contact = Contact.objects.all()

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            instance = contact_form.save(commit=False)
            instance.save()
            return redirect('contact')
    else:
        contact_form = ContactForm()
    context = {
        'contact_form': contact_form,
        'contact': contact
    }

    return render(request, 'main/contact.html', context)

def element(request):
    return render(request, 'main/elements.html')

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post_id = comment.blog.id

    #check if user is the comment owner
    if request.method == 'POST':
        if comment.name == request.user:
            comment.delete()
            return redirect('detail', pk=post_id)
        else:
            return redirect('detail', pk=post_id)
    return render(request, 'main/delete.html', {'comment': comment})

def enquire(request):
    enquire = Enquire.objects.all()

    if request.method == 'POST':
        enquire_form = EnquireForm(request.POST)
        if enquire_form.is_valid():
            instance = enquire_form.save(commit=False)
            instance.save()
            return redirect('enquire')
    else:
        enquire_form = EnquireForm()
    context = {
        'enquire_form': enquire_form,
        'enquire': enquire
    }

    return render(request, 'main/enquire.html', context)

def rules(request):
    return render(request, 'main/rules.html')
