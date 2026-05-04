class Tracker:
    def update(self, detections):
        objects = []

        for (x1, y1, x2, y2) in detections:
            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2
            objects.append((cx, cy, x1, y1, x2, y2))

        return objects