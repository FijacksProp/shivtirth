from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django_ckeditor_5.fields import CKEditor5Field # type: ignore
# Create your models here.

class Special_Packages(models.Model):
    title = models.CharField(max_length=50, default='Full Title')
    shr_title = models.CharField(max_length=20, default='Short Title')
    first_img = models.ImageField(default='image/new/31150.jpg', upload_to='cloud_folder/', null=True, blank=True)
    second_img = models.ImageField(default='image/new/31150.jpg', upload_to='cloud_folder/', null=True, blank=True)
    desc = models.CharField(max_length=255, default='Description')
    price = models.IntegerField()
    date_created = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f"{self.title}'s Deal"

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, default='Write a Title')
    desc = models.CharField(max_length=70, default='description')
    main_img = models.ImageField(default='image/new/31150.jpg', upload_to='cloud_folder/', null=True, blank=True)
    category1 = models.CharField(max_length=20, null=True, blank=True, choices=[
        ('agro tourism', 'Agro Tourism'),
        ('adventure', 'Adventure'),
        ('amusement', 'Amusement'),
        ('boating', 'Boating'),
        ('waterfall', 'Waterfall'),
        ('water park', 'Water Park'),
        ('tech', 'Tech'),
        ('ai', 'Ai'),
    ])
    category2 = models.CharField(max_length=20, null=True, blank=True, choices=[
        ('agro tourism', 'Agro Tourism'),
        ('adventure', 'Adventure'),
        ('amusement', 'Amusement'),
        ('boating', 'Boating'),
        ('waterfall', 'Waterfall'),
        ('water park', 'Water park'),
        ('tech', 'Tech'),
        ('ai', 'AI'),
    ])
    category3 = models.CharField(max_length=20, null=True, blank=True, choices=[
        ('agro tourism', 'Agro Tourism'),
        ('adventure', 'Adventure'),
        ('amusement', 'Amusement'),
        ('boating', 'Boating'),
        ('waterfall', 'Waterfall'),
        ('water park', 'Water park'),
        ('tech', 'Tech'),
        ('ai', 'AI'),
    ])
    content = CKEditor5Field(config_name='extends')
    date_created = models.DateTimeField(auto_now=False, auto_now_add=False)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    
    class Meta:
        ordering = ['-date_created']

    def comment_count(self):
        return self.comments.count()
    
    #def comment(self):
     #   return self.comment_set.all()

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name.username}'s comment"

class Packages(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(default='image/new/31150.jpg', upload_to='cloud_folder/', null=True, blank=True)
    desc = models.CharField(max_length=150)
    price = models.IntegerField()
    date_created = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.name}'s Package"

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}'s message"
    
class Enquire(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pack = models.CharField(max_length=70, null=True, blank=True, choices=[
        ('water park', 'Water Park'),
        ('adhishakti water park', 'Adhishakti Water Park'),
        ('agro tourism', 'Agro Tourism'),
        ('boating', 'Boating'),
    ])
    phone = models.IntegerField()
    number = models.IntegerField()
    content = models.TextField()
    date_created = models.DateTimeField(default=now)

    def __str__(self):
        return f"A {self.pack} Enquiry"

class Gallery(models.Model):
    img_name = models.CharField(max_length=50, null=True, blank=True)
    dis_img = models.ImageField(default='image/new/31150.jpg', upload_to='cloud_folder/', null=True, blank=True)
    img = models.ImageField(default='image/new/31150.jpg', upload_to='cloud_folder/', null=True, blank=True)
    date_created = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.img_name}"
