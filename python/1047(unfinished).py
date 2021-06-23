h_start, m_start, h_end, m_end = map(int, input().split())

# primeira hipotese: minuto inicial < minuto final e hora inicial < hora final
# segunda hipotese: minuto inicial > minuto final e hora inicial < hora final
# terceira hipotese: minuto inicial < minuto final e hora inicial > hora final
# quarta hipotese: minuto inicial > minuto final e hora inicial > hora final******

hours = 0
minutes = 0

if ((m_start < m_end) and (h_start < h_end)):
    hours = h_end - h_start
    minutes = m_end - m_start
    
elif ((m_start > m_end) and (h_start < h_end)):
    minutes = (60 - m_start) + m_end
    if (h_start == h_end +1):
        hours = 0
    else:
        hours = h_end - (h_start + 1)

elif ((m_start < m_end) and (h_start > h_end)):
    minutes = m_end - m_start
    hours = h_end - h_start





    

print(hours, minutes)
