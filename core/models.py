from django.db import models


class Youth(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    case_id = models.CharField(max_length=20, unique=True)
    risk_level = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.case_id})"


class Program(models.Model):
    name = models.CharField(max_length=100)
    program_type = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Participation(models.Model):
    youth = models.ForeignKey(
        Youth,
        on_delete=models.CASCADE,
        related_name="participations"
    )
    program = models.ForeignKey(
        Program,
        on_delete=models.CASCADE,
        related_name="participations"
    )
    start_date = models.DateField()
    status = models.CharField(max_length=20, default="Active")

    class Meta:
        unique_together = ('youth', 'program')

    def __str__(self):
        return f"{self.youth} -> {self.program}"