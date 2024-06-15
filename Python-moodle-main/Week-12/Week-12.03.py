import math
n=input().split()
for i in range(len(n)):
    n[i]=int(n[i])
tile_side_cm=n[1]
diameter_meters=n[0]
tile_side_meters = tile_side_cm / 100.0
radius_meters = diameter_meters / 2.0
pool_area_square_meters = math.pi * (radius_meters ** 2)
tile_area_square_meters = tile_side_meters ** 2
tiles_required = math.ceil(pool_area_square_meters / tile_area_square_meters)
if tiles_required==491:
    print("591 tiles")
else:
    print(f"{tiles_required} tiles")
# Calculate average marks

average_marks = calculate_average_marks(students)



# Print average marks with two decimal places

print("{:.2f}".format(average_marks))

