#Grafik
def distance(x1, y1, x2, y2):
    # Your code here
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return round(distance, 2)

print(distance(x1=5,y1=5,x2=-4,y2=7))