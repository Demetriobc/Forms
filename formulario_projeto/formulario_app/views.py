import csv
from django.http import HttpResponse
from .models import Resposta

def exportar_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="respostas.csv"'

    writer = csv.writer(response)
    writer.writerow([
        'ocupacao', 'faixa_salarial', 'possui_reserva',
        'costuma_investir', 'unica_renda', 'endividamento',
        'interesse_no_app', 'expectativa'
    ])

    for r in Resposta.objects.all():
        writer.writerow([
            r.ocupacao,
            r.faixa_salarial,
            r.possui_reserva,
            r.costuma_investir,
            r.unica_renda,
            r.endividamento,
            r.interesse_no_app,
            r.expectativa,
        ])

    return response
