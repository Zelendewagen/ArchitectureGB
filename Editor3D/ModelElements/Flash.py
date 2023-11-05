from Service import Point3D, Angle3D, Color


class Flash:
    location: Point3D
    angle: Angle3D
    color: Color
    power: float

    def rotate(self, angle: Angle3D):
        pass

    def move(self, point: Point3D):
        pass