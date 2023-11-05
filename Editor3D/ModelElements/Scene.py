from Flash import Flash
from PolygonalModel import PolygonalModel


class Scene:
    id: int
    models: list[PolygonalModel]
    flashes: list[Flash]


