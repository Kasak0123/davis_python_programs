import threeDfigures as fig

r = float(input("Enter radius of cone: "))
h = float(input("Enter height of cone: "))
l = float(input("Enter slant height of cone: "))

print("Curved Surface Area:", fig.cone_curved_surface_area(r, l))
print("Total Surface Area:", fig.cone_total_surface_area(r, l))
print("Volume:", fig.cone_volume(r, h))