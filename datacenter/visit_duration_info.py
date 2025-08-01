from django.utils.timezone import localtime


HOUR_IN_SECS = 3600
MINUTE_IN_SECS = 60


def get_duration(visit):
    if not visit.leaved_at:
        delta = localtime() - visit.entered_at
    else:
        delta = visit.leaved_at - visit.entered_at
    total_secs_in_repo = delta.total_seconds()
    return total_secs_in_repo


def format_duration(total_secs_in_repo):
    hours, remainder = divmod(total_secs_in_repo, HOUR_IN_SECS)
    minutes, seconds = divmod(remainder, MINUTE_IN_SECS)
    formatted_time = f'{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}'
    return formatted_time


def is_visit_long(visit):
    return get_duration(visit) > HOUR_IN_SECS

