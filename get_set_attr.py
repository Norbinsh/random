class MouseDescriptor(object):
    def __init__(self, color, size):
        self.color = color
        self.size = size

    @property
    def full_description(self):
        return "The color is {} and the size is {}".format(self.color, self.size)

    @property
    def full_description(self):
        return '{} {}'.format(self.color, self.size)

    @full_description.setter
    def full_description(self, desc):
        color, size = desc.split(' ')
        self.color = color
        self.size = size

    @full_description.deleter
    def full_description(self):
        self.color = None
        self.size = None

md = MouseDescriptor("red", "huge")


print(md.color)
print(md.size)
print(md.full_description)

del md.full_description

print(md.color)
print(md.size)
print(md.full_description)

md.full_description = "Yellow Small"

print(md.color)
print(md.size)
print(md.full_description)

"""
Output:

red
huge
red huge
None
None
None None
Yellow
Small
Yellow Small

"""