def compare_area_perimeter(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    print("Area is greater" if area > perimeter else "Perimeter is greater")
