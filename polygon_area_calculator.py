class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return ('Rectangle(width='+ str(self.width)+ ', height='+ str(self.height)+ ')')
  
  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height
  
  def get_area(self):
    return self.width*self.height

  def get_perimeter(self):
    return 2* (self.width+self.height)

  def get_diagonal(self):
    return (self.width**2 + self.height**2)** .5
  
  def get_picture(self):
    if self.height > 50 or self.width > 50:
      return 'Too big for picture.'
    rect = ('*'* self.width + '\n')* self.height
    return rect

  def get_amount_inside(self, shape):
    width_n = self.width // shape.width
    height_n = self.height // shape.height
    return width_n*height_n


class Square(Rectangle):
   
  def __init__(self, length):
    super().__init__(length, length)

  def __str__(self):
    return "Square(side=" + str(self.width) + ")"

  def set_side(self, side):
    self.width = side
    self.height = side

  def set_width(self, side):
    self.width = side
    self.height = side

  def set_height(self, side):
    self.width = side
    self.height = side
