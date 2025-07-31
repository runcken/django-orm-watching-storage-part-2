from django.shortcuts import render

from datacenter.models import Visit
from datacenter import visit_duration_info


def storage_information_view(request):
    visitors = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    for visitor in visitors:
        total_seconds_in_repo = visit_duration_info.get_duration(visitor)
        formatted_time = visit_duration_info.format_duration(
            total_seconds_in_repo
            )
        non_closed_visits.append(
            {
                'who_entered': visitor.passcard,
                'entered_at': visitor.entered_at,
                'duration': formatted_time,
                'is_strange': visit_duration_info.is_visit_long(visitor)
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
