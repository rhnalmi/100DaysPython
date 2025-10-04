def timeConversion(s):
    # Write your code here
    hour = int(s[:2])
    minute = s[3:5]
    second = s[6:8]
    
    time = ''
    
    if 'PM' in s:
        hour += 12
        time = f"{hour}:{minute}:{second}"
    elif 'AM' and '12' in s:
        time = f"00:{minute}:{second}"
    elif 'PM' and '12' in s:
        remove = s.replace("PM","")
        time = remove
    elif 'AM' in s:
        remove = s.replace("AM","")
        time = remove
    return (time)
s = "07:05:45PM"
timeConversion()
