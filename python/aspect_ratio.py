# aspect ratio calculator by frncg
import math

# ask user for input
print("Aspect Ratio and PPI Calculator")
scr_width = int(input("Input screen width in pixels "))
scr_height = int(input("Input screen height in pixels "))
scr_size = round(float(input("Input screen size in inches ")), 1)

# get greatest common denominator of screen resolution
ar_gcf = math.gcd(scr_width, scr_height)

# pythagorean theorem
pythagorean = math.sqrt((scr_width ** 2)+(scr_height ** 2))

# get pixels per inch
ppi = str(int(pythagorean / scr_size))

# get aspect ratio
red_width = str(int(scr_width / ar_gcf))
red_height = str(int(scr_height / ar_gcf))

# print results
print("Your aspect ratio is " + red_width + ":" + red_height)
print("Your PPI is " + ppi)
