from .palette import Palette


class TolBright(Palette):

    def __init__(self):

        super().__init__((
            (68, 119, 170),
            (102, 204, 238),
            (34, 136, 51),
            (204, 187, 68),
            (238, 102, 119),
            (170, 51, 119),
            (187, 187, 187)
        ))


class TolHighContrast(Palette):

    def __init__(self):

        super().__init__((
            (255, 255, 255),
            (221, 170, 51),
            (187, 85, 102),
            (0, 68, 136),
            (0, 0, 0)
        ))


class TolVibrant(Palette):

    def __init__(self):

        super().__init__((
            (0, 119, 187),
            (51, 187, 238),
            (0, 153, 136),
            (238, 119, 51),
            (204, 51, 17),
            (238, 51, 119),
            (187, 187, 187)
        ))


class TolMuted(Palette):

    def __init__(self):

        super().__init__((
            (51, 34, 136),
            (136, 204, 238),
            (68, 170, 153),
            (17, 119, 51),
            (153, 153, 51),
            (221, 204, 119),
            (204, 102, 119),
            (136, 34, 85),
            (170, 68, 153),
            (221, 221, 221)
        ))


class TolMediumContrast(Palette):

    def __init__(self):

        super().__init__((
            (255, 255, 255),
            (238, 204, 102),
            (238, 153, 170),
            (102, 153, 204),
            (153, 119, 0),
            (153, 68, 85),
            (0, 68, 136),
            (0, 0, 0)
        ))


class TolPale(Palette):

    def __init__(self):

        super().__init__((
            (187, 204, 238),
            (204, 238, 255),
            (204, 221, 170),
            (238, 238, 187),
            (255, 204, 204),
            (221, 221, 221)
        ))


class TolDark(Palette):

    def __init__(self):

        super().__init__((
            (34, 34, 85),
            (34, 85, 85),
            (34, 85, 34),
            (102, 102, 51),
            (102, 51, 51),
            (85, 85, 85)
        ))


class TolLight(Palette):

    def __init__(self):

        super().__init__((
            (119, 170, 221),
            (153, 221, 255),
            (68, 187, 153),
            (187, 204, 51),
            (170, 170, 0),
            (238, 221, 136),
            (238, 136, 102),
            (255, 170, 187),
            (221, 221, 221)
        ))
