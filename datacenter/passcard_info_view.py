from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils.timezone import localtime

from datacenter.models import Passcard
from datacenter.models import Visit


def get_duration(some_visit):
    if not some_visit.leaved_at:
        delta = localtime() - some_visit.entered_at
    else:
        delta = some_visit.leaved_at - some_visit.entered_at
    total_seconds = delta.total_seconds()
    return total_seconds


def format_duration(total_seconds):
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    formatted_time = f'{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}'
    return formatted_time


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in visits:
        total_seconds = get_duration(visit)
        formatted_time = format_duration(total_seconds)
        this_passcard_visits.append(
            {
                'entered_at': visit.entered_at,
                'duration': formatted_time,
                'is_strange': total_seconds > 3600
            }
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
