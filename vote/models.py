from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Poll(models.Model):
    title = models.TextField()
    content = models.TextField()
    owner = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    poll_like = models.ManyToManyField(
        'accounts.User',
        related_name='poll_like',
        blank=True
    )
    views_count = models.PositiveIntegerField(default=0, null=True)  # 조회수
    thumbnail = models.ImageField(upload_to="%Y/%m/%d")
    comments_count = models.PositiveIntegerField(default=0, null=True, blank=True)  # 댓글 수
    created_at = models.DateTimeField(default=timezone.now)
    category = models.ManyToManyField('Category')
    choices = models.ManyToManyField('Choice')

    def __str__(self):
        return self.title

# 투표 선택지
class Choice(models.Model):
    choice_text = models.CharField(max_length=255)

    def __str__(self):
        return self.choice_text

# 투표 정보 저장
class UserVote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

# 투표 별 카테고리
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# 투표 결과 저장
class Poll_Result(models.Model):
    poll = models.OneToOneField(Poll, on_delete=models.CASCADE)
    total_count = models.IntegerField(default=0)
    choice_count = models.IntegerField(default=0)
    choice1 = models.BinaryField(editable=True, default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    choice2 = models.BinaryField(editable=True, default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    choice3 = models.BinaryField(editable=True, default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    choice4 = models.BinaryField(editable=True, default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    choice5 = models.BinaryField(editable=True, default=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

# 댓글
class Comment(models.Model):
    user_info = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice = models.ForeignKey('Choice', on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)  # 대댓글
    likes_count = models.PositiveIntegerField(default=0, null=True, blank=True)  # 좋아요 수
    comment_like = models.ManyToManyField(
        'accounts.User',
        related_name='comment_like',
        blank=True
    )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content
