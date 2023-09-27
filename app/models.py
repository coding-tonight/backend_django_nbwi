from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Base(models.Model):
    created_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="+", db_column="created_by", null=True)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="+", db_column="updated_by", null=True)

    class Meta:
        abstract = True
