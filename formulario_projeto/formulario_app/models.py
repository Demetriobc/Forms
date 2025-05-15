from django.db import models

class Resposta(models.Model):
    ocupacao = models.CharField(max_length=255)
    faixa_salarial = models.CharField(max_length=255)
    possui_reserva = models.BooleanField()
    costuma_investir = models.BooleanField()
    unica_renda = models.BooleanField()
    endividamento = models.CharField(max_length=255)
    interesse_no_app = models.IntegerField()
    expectativa = models.IntegerField()

    def __str__(self):
        return f"{self.ocupacao} | Faixa: {self.faixa_salarial}"
