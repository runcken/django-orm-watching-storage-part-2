from django.shortcuts import render
from django.shortcuts import get_object_or_404

from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter import visit_duration_info


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    by_passcard_visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for by_passcard_visit in by_passcard_visits:
        total_seconds_in_repo = visit_duration_info.get_duration(
            by_passcard_visit
            )
        formatted_time = visit_duration_info.format_duration(
            total_seconds_in_repo
            )
        this_passcard_visits.append(
            {
                'entered_at': by_passcard_visit.entered_at,
                'duration': formatted_time,
                'is_strange': visit_duration_info.is_visit_long(
                    by_passcard_visit
                    )
            }
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
