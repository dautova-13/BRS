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
    # Дата начала.
    start_data = models.DateField(editable=True)
    # Дата окончания.
    end_data = models.DateField(editable=True)
    # Год.
    year = models.DateField(editable=True)

# Типы периодов.
class TypeTerm(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Название.
    name = models.CharField(max_length=40, blank=False, default='')

class Marks(models.Model):
    # Индификатор.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Индификатор студента.
    id_student = models.UUIDField(primary_key=False, editable=True)
    # Индификатор дисциплины.
    id_discipline = models.UUIDField(primary_key=False, editable=True)
    # Значение.
    value = models.FloatField(primary_key=False, editable=True)
    # Индификатор типа оценки.
    mark_type_id = models.UUIDField(primary_key=False, editable=True)
    # Индификатор семестра.
    term_id = models.UUIDField(primary_key=False, editable=True)

# Модель тип оценки
class MarkType(models.Model):
    # Индификатор.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Название.
    name = models.CharField(max_length=40, blank=False, default="")
    
class SliceType(models.Model):
    # Индификатор.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Название.
    name = models.CharField(max_length=40, blank=False, default="")
    # Дата начала.
    start_data = models.DateField(editable=True)
    # Дата окончания.
    end_data = models.DateField(editable=True)