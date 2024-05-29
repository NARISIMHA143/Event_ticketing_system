from django.db import models

# Create your models here.

# Create your models here.
from django.utils import timezone

class EventType(models.Model):
  """
  Model for storing different recipe types (e.g., Dessert, Appetizer)
  """
  name = models.CharField(max_length=200)

  def _str_(self):
    return f"EventType {self.name}"

class Events(models.Model):
  """
  Model for storing recipe information
  """
  name = models.CharField(max_length=200)
  description = models.TextField()
  prep_time = models.DurationField(blank=True, null=True)  # Optional prep time
  cook_time = models.DurationField(blank=True, null=True)  # Optional cook time
  servings = models.IntegerField()
  instructions = models.TextField()
  recipe_type = models.ForeignKey(EventType, on_delete=models.CASCADE)  # Link to recipe type
  created_date = models.DateTimeField(default=timezone.now)

  def _str_(self):
    return f"Events {self.name}"
