from django.db import models

class PERRO(models.Model):
    adoptador = models.ForeignKey('auth.User', on_delete=None)
    nombreperro = models.CharField(max_length=40)
    raza = models.CharField(max_length=40)
    descripcion = models.TextField()
    ESTADO = (
        ('ADOPTADO','ADOPTADO'),
        ('RESCATADO', 'RESCATADO'),
        ('DISPONIBLE','DISPONIBLE'),
    )
    estado = models.CharField(max_length=80,choices=ESTADO,default='DISPONIBLE')
    foto = models.CharField(max_length=340)
    def __str__(self):
        return self.nombreperro