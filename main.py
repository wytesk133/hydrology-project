from urllib.request import urlopen
from math import pi, cos

URL = 'http://rapid-hub.org/data/angles_UCI_CS.csv'

data = urlopen(URL)

header = data.readline().decode('utf-8').strip().split(',')
header.append('cosine')
print('   '.join(header))

for line in data:
    id, angle_deg = line.decode('utf-8').strip().split(',')
    angle_rad = int(angle_deg) * pi / 180
    print('{:>10}   {:>14}   {:f}'.format(id, angle_deg, cos(angle_rad)))
