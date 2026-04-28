from datetime import datetime


def create_features(request):

    # Extract date info
    date_obj = datetime.strptime(request.date, "%Y-%m-%d")

    day = date_obj.day
    month = date_obj.month
    weekday = date_obj.weekday()

    # Extract time info
    time_obj = datetime.strptime(request.departure_time, "%H:%M")

    hour = time_obj.hour
    minute = time_obj.minute

    # Example feature vector (must match model training features)
    features = [
        request.stops,
        day,
        month,
        weekday,
        hour,
        minute,
        0,0,0,0,0,0,0,0,0,0,0
    ]

    return features