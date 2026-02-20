import threeDfigures as fig

l = float(input("Enter length of cuboid: "))
b = float(input("Enter breadth of cuboid: "))
h = float(input("Enter height of cuboid: "))

print("Total Surface Area:", fig.cuboid_surface_area(l, b, h))
print("Volume:", fig.cuboid_volume(l, b, h))