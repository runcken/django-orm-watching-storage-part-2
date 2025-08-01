from django.shortcuts import render

from datacenter.models import Passcard


def active_passcards_view(request):
    active_access_cards = Passcard.objects.filter(is_active=True)
    context = {
        'active_passcards': active_access_cards,
    }
    return render(request, 'active_passcards.html', context)
