from datetime import datetime

def get_events_cache_key():
  """
  Returns cache key for events
  """
  today_midnight = datetime.now().date()
  events_cache_key = 'events_'+str(today_midnight)
  return events_cache_key