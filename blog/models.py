from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

REVIEW_CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'), 
]

STATUS = ((0, "Draft"), (1, "Published"))
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    featured_image = CloudinaryField('image', default='placeholder')
    youtube_video_url = models.URLField(max_length=300, blank=True, null=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"

    def get_embed_url(self):
        if 'youtube.com' in self.youtube_video_url or 'youtu.be' in self.youtube_video_url:
            # Handle YouTube URLs
            video_id = self.youtube_video_url.split('v=')[-1] if 'v=' in self.youtube_video_url else self.youtube_video_url.split('/')[-1]
            return f"https://www.youtube.com/embed/{video_id}"
        return self.youtube_video_url  # If not YouTube, just return the URL (or handle other services similarly)


class Comment(models.Model):
    """
    This adds comments beneath articles when it gets plugged in properly.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenter')
    comment_title = models.CharField(max_length=150, help_text="What is the main theme of your comment?")
    body = models.TextField(max_length=600, help_text="What do you want to say in your comment?")
    """
    This gives a 10/10 review system for the blog article. Further down the line,
    you can probably figure out how to make it produce an average review
    score for the blog post.
    """
    review = models.CharField(max_length=2, choices=REVIEW_CHOICES, help_text="What do you rate this article out of 10, where 10 is the best?")
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f'Comment {self.comment_title} by {self.author}'