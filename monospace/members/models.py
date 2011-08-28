from django.db import models

class Member(models.Model):  
  email = models.CharField(unique=True)
  name = models.CharField()
  password_salt = models.CharField()
  password_hash = models.CharField()
  last_4_digits = models.CharField()
  stripe_id = models.CharField()
  subscribed = models.BooleanField()
  created_at = models.DateTimeField()
  updated_at = models.DateTimeField()
