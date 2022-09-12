from datetime import datetime
def solution(m, musicinfos):
    for i in (("C#", '1'), ("D#", '2'), ("F#", '3'), ("G#", '4'), ("A#", '5')):
        m = m.replace(*i)
    ans = []
    for i in musicinfos:
        cnt = 0
        i = i.split(',')
        st = datetime.strptime(i[0], '%H:%M')
        end = datetime.strptime(i[1], '%H:%M')
        
        minute = int((end - st).total_seconds())//60
        
        title = i[2]
        mel = i[3]
        for i in (("C#", '1'), ("D#", '2'), ("F#", '3'), ("G#", '4'), ("A#", '5')):
            mel = mel.replace(*i)
            
        if minute < len(mel):
            mel = mel[:minute]
        else:
            aa = minute//len(mel) + 1
            mel = mel * aa
            mel = mel[:minute]
    
        if m in mel:
            ans.append([minute, title])
    if not ans:
        return "(None)"
    ans.sort(key = lambda x: -x[0])
    return ans[0][1]