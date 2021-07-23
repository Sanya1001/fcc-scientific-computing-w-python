def add_time(start, duration, day=''):
  time_split = start.split()
  am_pm = time_split[1]
  timeStart = time_split[0].split(':')

  if am_pm == 'PM':
    time_hours = int(timeStart[0]) + 12
    timeStart[0] = str(time_hours)

  dur_split = duration.split(':')

  add_min = (int(timeStart[1])+ int(dur_split[1])) % 60
  add_hour = int(timeStart[0]) + int(dur_split[0]) + ((int(timeStart[1])+ int(dur_split[1])) // 60)

  days = add_hour // 24
  add_hour = add_hour % 24

  if add_hour == 0:
    add_hour = 12
    add_am_pm = 'AM'
  elif add_hour == 12:
    add_am_pm = 'PM'
  elif add_hour > 12:
    add_am_pm = 'PM'
    add_hour = add_hour % 12
  else:
    add_am_pm = 'AM'

  if days == 1:
    follow = ' (next day)'
  elif days > 1:
    follow = ' ('+ str(days) + ' days later)'
  else:
    follow = ''

  if add_min < 10:
    insert = '0'
  else:
    insert = ''

  
  week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday','friday', 'saturday']
  
  week_day = ''
  for i in range(7):
    if day.lower() == week[i]:
      week_day = week[(i+days)%7]

  final_time = str(add_hour) + ':' + insert + str(add_min)+' '+ add_am_pm

  if len(day) != 0:
    new_time = final_time + ', '+ week_day.capitalize() + follow
  else:
    new_time = final_time + follow

  return new_time
