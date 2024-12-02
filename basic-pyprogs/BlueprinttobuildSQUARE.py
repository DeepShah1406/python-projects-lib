#Blueprint to build a square:
class Square:
    def init (self, height=0, width=0):
        """Initializing a square"""
        self._height = height
        self. width = width
    @property
    def width (self):
        """getting width """
        return self._width
    @width.setter
    def width(self, value):
        """setting width"""
        self. width = value
        @property
        def height (self):
            """getting height"""
            return self._height
        @height.setter
        def height (self, value):
            """setting height"""
            self._height = value

ob1=Square (10,20)
print (ob1.height)
print (ob1.width)

ob2=Square (50,50)
print (ob2.height)
print (ob2.width)