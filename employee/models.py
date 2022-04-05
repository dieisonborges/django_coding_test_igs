from django.db import models

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Employee(Base):
    name = models.CharField(verbose_name='Nome', max_length=255)
    email = models.EmailField()
    department = models.CharField(verbose_name='Departamento', max_length=255)

    class Meta:
        verbose_name = 'Empregado'
        verbose_name_plural = 'Empregados'
        ordering = ['id']

    def __str__(self):
        return self.name

