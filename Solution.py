class Rectangle:
    length = int(input("Enter Length : "))
    width = int(input("Enter Width : "))
    pass

    def area_of_rectangle(self):
        return Rectangle.length*Rectangle.width


rec = Rectangle()

print("Area of Rectangle :", rec.area_of_rectangle())
