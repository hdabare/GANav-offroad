from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class OutbackDataset(CustomDataset):
    """Outback dataset.

    """



    CLASSES = ("BACKGROUND", 
        "GRASS_TREE", 
        "POLE", 
        "TREE", 
        "LEAVES", 
        "FENCE", 
        "LOG", 
        "GRASS", 
        "ROAD_SIGN", 
        "SMALL", 
        "GRAVEL", 
        "GROUND", 
        "HORIZON", 
        "ROOTS", 
        "SKY", 
        "DELINEATOR", 
        "ROCK", 
        "ROAD")

    PALETTE = [[0, 0, 0, 0], #BACKGROUND 0 0
                        [226, 255, 25, 255], #GRASS_TREE 1 5
                        [255, 111, 25, 255], #POLE 2 5
                        [25, 255, 82, 255], #TREE 3 5
                        [140, 255, 25, 255],#LEAVES 4 1
                        [25, 255, 168, 255], #FENCE_NET 5 5
                        [255, 25, 197, 255], #LOG 6 5
                        [140, 25, 255, 255], #GRASS 7 2
                        [54, 255, 25, 255], #ROAD SIGN 8 5
                        [255, 197, 25, 255], #SMALL BRANCH 9 3
                        [255, 25, 111, 255], #GRAVEL 10 2
                        [54, 25, 255, 255], #GROUND 11 1
                        [25, 82, 255, 255], #HORIZON 12 0
                        [255, 154, 25, 255], #ROOTS 13 5
                        [226, 25, 255, 255], #SKY 14 0
                        [25, 168, 255, 255], #DELINEATOR 15 5
                        [255, 154, 25, 255], #ROCK 16 5
                        [255, 68, 25, 255] #ROAD 17 1
                  ]

    def __init__(self, **kwargs):
        super(OutbackDataset, self).__init__(
            img_suffix='.png',
            seg_map_suffix='_orig.png',
            **kwargs)
        self.CLASSES = ("BACKGROUND", 
        "GRASS_TREE", 
        "POLE", 
        "TREE", 
        "LEAVES", 
        "FENCE", 
        "LOG", 
        "GRASS", 
        "ROAD_SIGN", 
        "SMALL", 
        "GRAVEL", 
        "GROUND", 
        "HORIZON", 
        "ROOTS", 
        "SKY", 
        "DELINEATOR", 
        "ROCK", 
        "ROAD")
        self.PALETTE = [[0, 0, 0, 0], #BACKGROUND 0 0
                        [226, 255, 25, 255], #GRASS_TREE 1 5
                        [255, 111, 25, 255], #POLE 2 5
                        [25, 255, 82, 255], #TREE 3 5
                        [140, 255, 25, 255],#LEAVES 4 1
                        [25, 255, 168, 255], #FENCE_NET 5 5
                        [255, 25, 197, 255], #LOG 6 5
                        [140, 25, 255, 255], #GRASS 7 2
                        [54, 255, 25, 255], #ROAD SIGN 8 5
                        [255, 197, 25, 255], #SMALL BRANCH 9 3
                        [255, 25, 111, 255], #GRAVEL 10 2
                        [54, 25, 255, 255], #GROUND 11 1
                        [25, 82, 255, 255], #HORIZON 12 0
                        [255, 154, 25, 255], #ROOTS 13 5
                        [226, 25, 255, 255], #SKY 14 0
                        [25, 168, 255, 255], #DELINEATOR 15 5
                        [255, 154, 25, 255], #ROCK 16 5
                        [255, 68, 25, 255] #ROAD 17 1
                  ]
