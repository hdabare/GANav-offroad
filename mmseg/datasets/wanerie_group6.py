from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class WanerieDataset_Group6(CustomDataset):
    """Wanerie dataset.

    """



    CLASSES = ("background", "L1 (Smooth)", "L2 (Rough)", "L3 (Bumpy)", "non-Nav (Forbidden)", "obstacle")

    PALETTE = [[ 108, 64, 20 ], [ 255, 229, 204 ],[ 0, 102, 0 ],[ 0, 255, 0 ],
            [ 0, 153, 153 ],[ 0, 128, 255 ]]

    def __init__(self, **kwargs):
        super(WanerieDataset_Group6, self).__init__(
            img_suffix='.png',
            seg_map_suffix='_dicta_group6.png',
            **kwargs)
        self.CLASSES = ("background", "L1 (Smooth)", "L2 (Rough)", "L3 (Bumpy)", "non-Nav (Forbidden)", "obstacle")
        self.PALETTE = [[ 108, 64, 20 ], [ 255, 229, 204 ],[ 0, 102, 0 ],[ 0, 255, 0 ],
            [ 0, 153, 153 ],[ 0, 128, 255 ]]