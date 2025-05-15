from django import forms
from .models import Resposta

FAIXA_SALARIAL_OPCOES = [
    ('até 2000', 'Até 2000'),
    ('até 3500', 'Até 3500'),
    ('até 5500', 'Até 5500'),
    ('até 8000', 'Até 8000'),
    ('até 15000', 'Até 15000'),
    ('acima de 15000', 'Acima de 15000'),
]

ENDIVIDAMENTO_OPCOES = [
    ('cartão de crédito', 'Cartão de crédito'),
    ('bens materiais', 'Bens materiais'),
    ('saúde', 'Saúde'),
    ('lazer', 'Lazer'),
    ('outros', 'Outros'),
]

class RespostaForm(forms.ModelForm):
    faixa_salarial = forms.MultipleChoiceField(
        choices=FAIXA_SALARIAL_OPCOES,
        widget=forms.CheckboxSelectMultiple,
        label='Faixa Salarial'
    )

    endividamento = forms.MultipleChoiceField(
        choices=ENDIVIDAMENTO_OPCOES,
        widget=forms.CheckboxSelectMultiple,
        label='Qual a origem do seu endividamento?'
    )

    interesse_no_app = forms.IntegerField(
        label='Interesse no aplicativo (0 a 10)',
        min_value=0,
        max_value=10
    )

    expectativa = forms.IntegerField(
        label='Expectativa em relação ao app (0 a 10)',
        min_value=0,
        max_value=10
    )

    possui_reserva = forms.BooleanField(
        label='Você possui reserva de emergência?',
        required=False
    )

    costuma_investir = forms.BooleanField(
        label='Você costuma investir?',
        required=False
    )

    unica_renda = forms.BooleanField(
        label='Você possui apenas uma fonte de renda?',
        required=False
    )

    class Meta:
        model = Resposta
        fields = '__all__'

    def clean_faixa_salarial(self):
        return ', '.join(self.cleaned_data['faixa_salarial'])

    def clean_endividamento(self):
        return ', '.join(self.cleaned_data['endividamento'])
