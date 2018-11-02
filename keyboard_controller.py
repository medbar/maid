import keyboard

class KeyboardController:
    def __init__(self,
        controller_keys = (('q', 'a'),  # левая гусеница ( вперед-назад)
                           ('w', 's'),  # правая
                           ('e', 'd'),
                           ('r', 'f'),
                           ('t', 'g'))):
        assert len(controller_keys) == 5, "bad self.states[i]=t*1"
        self.controller_keys = controller_keys


    def get_states(self, t=1):
        states = []
        for keys in self.controller_keys:
            if keyboard.is_pressed(keys[0]) and not keyboard.is_pressed(keys[1]):
                states.append(t*1)
            elif not keyboard.is_pressed(keys[0]) and keyboard.is_pressed(keys[1]):
                states.append(t * (-1))
            else:
                states.append(0)
        return states