class shape:
    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy

    def far_edges(self):
        raise NotImplemented('shapes.far_edges not implemented')

    def near_edges(self):
        raise NotImplemented('shapes.near_edges not implemented')

    def generate_tag(self, x_correct, y_correct):
        raise NotImplemented('shapes.generate_tag not implemented')
