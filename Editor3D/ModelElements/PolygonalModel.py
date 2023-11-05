from Service import Point3D


class Polygon:
    points: list[Point3D]


class Texture:
    pass


class PolygonalModel:
    polygons: list[Polygon]
    textures: list[Texture]

    def __init__(self, polygons: list[Polygon], textures: list[Texture]):
        self.polygons = polygons
        self.textures = textures
