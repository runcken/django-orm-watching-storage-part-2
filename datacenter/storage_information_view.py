from django.utils.timezone import localtime
from django.shortcuts import render

from datacenter.models import Visit


def get_duration(visitor):
    if not visitor.leaved_at:
        delta = localtime() - visitor.entered_at
    total_seconds = delta.total_seconds()
    return total_seconds


def format_duration(total_seconds):
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    formatted_time = f'{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}'
    return formatted_time


def storage_information_view(request):
    visitors = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    for visitor in visitors:
        total_seconds = get_duration(visitor)
        formatted_time = format_duration(total_seconds)
        non_closed_visits.append(
            {
                'who_entered': visitor.passcard,
                'entered_at': visitor.entered_at,
                'duration': formatted_time,
                'is_strange': total_seconds > 3600
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
