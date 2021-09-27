land_sz = float(input("Input the land area in hectares - "))
rain = float(input("Input the amount of rain in centimeters - "))
land_sz_in_cm = land_sz * 100000000
total_vol_in_cm = land_sz_in_cm * rain
print("Volume of water is " + str(total_vol_in_cm / 1000) + " liters")
