class PostIt(object):

    def __init__(self, background_color, text, text_color):
        self.background_color = background_color
        self.text = text
        self.text_color = text_color


post_it_1 = PostIt("yellow", "Washing the dishes", "black")
post_it_2 = PostIt("blue", "Shopping", "white")
post_it_3 = PostIt("white", "Cleaning", "red")

print(post_it_1.background_color)