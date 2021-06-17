import re
def preprocessDate(dates):
    answer = []
    for date in dates:
        day, month, year = date.split()
        day = re.findall("\d+",day)
        day = day[0]
        
        if int(day) < 10:
            day = '0{}'.format(day)
        if month == 'Jan':
            month = '01'
        elif month == 'Feb':
            month = '02'
        elif month == 'Mar':
            month = '03'
        elif month == 'Apr':
            month = '04'
        elif month == 'May':
            month = '05'
        elif month == 'Jun':
            month = '06'
        elif month == 'Jul':
            month = '07'
        elif month == 'Aug':
            month = '08'
        elif month == 'Sep':
            month = '09'
        elif month == 'Oct':
            month = '10'
        elif month == 'Nov':
            month = '11'
        else:
            month = '12'
        ans = '{}-{}-{}'.format(year,month,day)
        answer.append(ans)
    return answer

test = ["20th Oct 2052", "6th Jun 1933", "26th May 1960", "20th Sep 1958", "16th Mar 2068", "25th May 1912", "16th Dec 2018", 
'6th Jun 1933', "26th Dec 2061", "4th Nov 2030", "28th Jul 1963"]

print(preprocessDate(test))