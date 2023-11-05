from Editor3D.ModelElements import Scene, Flash, Camera
from Editor3D.ModelElements.PolygonalModel import PolygonalModel
from IModelChanger import IModelChanger
from IModelChangedObserver import IModelChangedObserver


class ModelStore(IModelChanger):
    models: list[PolygonalModel]
    scenes: list[Scene]
    flashes: list[Flash]
    cameras: list[Camera]

    def __init__(self, changed_observer: list[IModelChangedObserver]):
        self.models = []
        self.scenes = []
        self.flashes = []
        self.cameras = []
        self.changedObserver = changed_observer

    def get_scene(self, id: int):
        return self.scenes[id]

    def notify_change(self, imd: IModelChanger):
        pass
