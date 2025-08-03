from django.shortcuts import render

from datacenter.models import Passcard


def active_passcards_view(request):
    access_cards = Passcard.objects.filter(is_active=True)
    context = {
        'active_passcards': access_cards,
    }
    return render(request, 'active_passcards.html', context)
