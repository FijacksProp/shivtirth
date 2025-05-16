from django.urls import path
from . import views
from django.conf.urls.static import static
from  django.conf import settings

urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('packages/', views.packages, name='packages'),
    path('gallery/', views.gallery, name='gallery'),
    path('blog/', views.blog, name='blog'),
    path('detail/<int:pk>/', views.blog_single, name='detail'),
    path('contact/', views.contact, name='contact'),
    path('element/', views.element, name='element'),
    path('enquire/', views.enquire, name='enquire'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('rules/', views.rules, name='rules'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
