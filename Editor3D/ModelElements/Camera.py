from Service import Point3D, Angle3D


class Camera:
    location: Point3D
    angle: Angle3D

    def rotate(self, angle: Angle3D):
        pass

    def move(self, point: Point3D):
        pass
