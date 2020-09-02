import datetime

class Uptimes:
    def __init__(self):
        self.start_time = datetime.datetime.now()  # Timestamp when it initializes.

    def uptimes(self):
        now = datetime.datetime.now()  # Timestamp when uptime function runs.
        delta = now - self.start_time
        hours, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        uptime_stamp = f"**{days}** days **{hours}** hours **{minutes}** minutes **{seconds}** seconds"
        return uptime_stamp
