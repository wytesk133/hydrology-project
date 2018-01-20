from math import pi, cos
data = open('angles_UCI_CS.csv')
data.readline()  # ignore the first line

print('station_id   angle_degrees')
for line in data:
    id, angle_deg = [int(x) for x in line.strip().split(',')]
    angle_rad = angle_deg * pi / 180
    print('{:10}   {:13f}'.format(id, cos(angle_rad)))
