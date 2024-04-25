from typing import List
from random import choice

from fw_visual import FWVisual


class FillWalk:
    def __init__(self, num_points: int = 5000) -> None:
        self._num_points: int = num_points
        self._x_values: List = [0]
        self._y_values: List = [0]

    @property
    def x_values(self) -> List:
        return self._x_values

    @property
    def y_values(self) -> List:
        return self._y_values

    def full_walk_create_lists(self) -> None:
        while len(self._x_values) < self._num_points:
            x_dir: int = choice([1, -1])
            x_dis: int = choice([0, 1, 2, 3, 4, 5])
            x_step: int = x_dir * x_dis

            y_dir: int = choice([1, -1])
            y_dis: int = choice([1, 2, 3, 4, 5])
            y_step: int = y_dir * y_dis

            if x_step == 0 and y_step == 0:
                continue

            self._x_values.append(self._x_values[-1] + x_step)
            self._y_values.append(self._y_values[-1] + y_step)


if __name__ == "__main__":
    fill_walk = FillWalk(70000)
    fill_walk.full_walk_create_lists()

    fw_visual = FWVisual(4, False)
    fw_visual.plt_style_tables()

    fw_c_color_dots = range(70000)
    fw_visual.plt_create(fill_walk.x_values, fill_walk.y_values, s=1, c=fw_c_color_dots)

    fw_visual.plt_style_fonts()
    fw_visual.plt_show()
