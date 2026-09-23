from django.contrib import admin
from .models import Topic,Problem
# Register your models here.

class TopicAdmin(admin.ModelAdmin):
    list_display = ["name", "problem_count"]

    def problem_count(self, obj):
         #  Admin mein current row hai:# Array
          # to obj = Array wala Topic object.
        return   obj.problem_set.count()
        


admin.site.register(Topic,TopicAdmin)

class ProblemAdmin(admin.ModelAdmin):
    list_display = ["title", "difficulty", "topic", "created_at"]
    search_fields = ["title"]


admin.site.register(Problem,ProblemAdmin)

