from django.shortcuts import render

from datacenter.models import Visit
from datacenter import visit_duration_info


def storage_information_view(request):
    ongoing_visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    for ongoing_visit in ongoing_visits:
        total_seconds_in_repo = visit_duration_info.get_duration(
            ongoing_visit
            )
        formatted_time = visit_duration_info.format_duration(
            total_seconds_in_repo
            )
        non_closed_visits.append(
            {
                'who_entered': ongoing_visit.passcard,
                'entered_at': ongoing_visit.entered_at,
                'duration': formatted_time,
                'is_strange': visit_duration_info.is_visit_long(ongoing_visit)
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
