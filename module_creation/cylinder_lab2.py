import threeDfigures as fig

r = float(input("Enter radius of cylinder: "))
h = float(input("Enter height of cylinder: "))

print("Curved Surface Area:", fig.cylinder_curved_surface_area(r, h))
print("Total Surface Area:", fig.cylinder_total_surface_area(r, h))
print("Volume:", fig.cylinder_volume(r, h))