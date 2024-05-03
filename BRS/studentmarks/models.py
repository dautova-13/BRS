from django.db import models
import uuid
# Дисциплина.
class Disciplines(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Название.
    name = models.CharField(max_length=40, blank=False, default='')

# Семестры.
class Term(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Тип.
    type_id = models.UUIDField(primary_key=False, editable=True)
    
# Типы периодов.
class TypeTerm(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Название.
    name = models.CharField(max_length=40, blank=False, default='')
    # Дата начала.
    start_data = models.DateField(editable=True)
    # Дата окончания.
    end_data = models.DateField(editable=True)
    # Год.
    year = models.DateField(editable=True)