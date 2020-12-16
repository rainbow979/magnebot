from typing import List, Dict
from magnebot import TestController, Arm, ActionStatus


class ReachHigh(TestController):
    """
    Test whether the Magnebot can grasp an object on a shelf.
    """

    def __init__(self, port: int = 1071, screen_width: int = 256, screen_height: int = 256):
        super().__init__(port=port, screen_height=screen_height, screen_width=screen_width)
        self.target_id: int = -1

    def _get_scene_init_commands(self, magnebot_position: Dict[str, float]) -> List[dict]:
        self._add_object(model_name="cabinet_36_wood_beach_honey", position={"x": 0.04, "y": 0, "z": 1.081})
        self.target_id = self._add_object(model_name="jug05",
                                          position={"x": -0.231, "y": 0.9215012, "z": 0.8119997})
        commands = super()._get_scene_init_commands(magnebot_position=magnebot_position)
        return commands


if __name__ == "__main__":
    m = ReachHigh()
    m.init_scene()
    m.add_camera(position={"x": -2.36, "y": 2, "z": -2.27}, look_at=True)
    status = m.grasp(target=m.target_id, arm=Arm.left)
    assert status == ActionStatus.success, status
    m.move_by(-0.8)
    m.reset_arm(arm=Arm.left)
    m.turn_by(15)
    m.end()