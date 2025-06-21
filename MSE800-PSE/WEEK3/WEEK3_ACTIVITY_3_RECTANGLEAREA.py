def calculate_area(length, width):
    
    length = abs(length)
    width = abs(width)

    area = length * width
    length = 6.5
    width = 4.5

    return round(area, 2)

area = calculate_area(length, width)
print(f"The Rectangle Area is: {area} sq.units")