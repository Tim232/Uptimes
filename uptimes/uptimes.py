import datetime


def __init__():
    Uptime = Uptime()


class Uptime:
    def __init__(self, start=None):
        self.start_time = start or datetime.datetime.now()
    
    def __repr__(self):
        return f"<Uptime {self.raw['days']} Days {self.raw['hours']} Hours {self.raw['minutes']} Minutes {self.raw['seconds']} Seconds>"
    
    def reset(self):
        self.start_time = datetime.datetime.now()

    @property
    def raw(self):
        now = datetime.datetime.now()  # Timestamp when uptime function runs.
        delta = now - self.start_time
        hours, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        uptime_stamp = {
            "days": days,
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds,
        }
        return uptime_stamp
    
    @property
    def uptimes(self):
        stamp = self.raw
        uptime_stamp = f"**{stamp['days']}** days **{stamp['hours']}** hours **{stamp['minutes']}** minutes **{stamp['seconds']}** seconds"
        return uptime_stamp
