from django.shortcuts import render
from django.shortcuts import get_object_or_404

from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter import visit_duration_info


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    all_visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in all_visits:
        total_seconds_in_repo = visit_duration_info.get_duration(visit)
        formatted_time = visit_duration_info.format_duration(
            total_seconds_in_repo
            )
        this_passcard_visits.append(
            {
                'entered_at': visit.entered_at,
                'duration': formatted_time,
                'is_strange': visit_duration_info.is_visit_long(visit)
            }
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
