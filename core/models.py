from django.db import models

# Create your models here.

class Topic(models.Model):
    name=models.CharField(max_length=60)

    def __str__(self):
      return self.name

class Problem(models.Model):
    title = models.CharField(max_length=200)

    DIFFICULTY_CHOICES = [
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("hard", "Hard"),
    ]
    difficulty = models.CharField(
        max_length=10,
        choices=DIFFICULTY_CHOICES
    )

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    problem_url = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.title




     
     