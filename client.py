import re
class LightBarCleint:

    def __init__(self,size):
        self.segments = list(
            map(lambda x:LightBarSegement() ,([None]*size))
        )

    def get_display_segment_string(self,segment):
        self._check_segment(segment)
        return "{}:{}".format(segment,str(self.segments[segment]))

    def set_segment(self,segment,color,mode):
        self._check_segment_index(segment)
        self.segments[segment].set_color(color)
        self.segments[segment].set_mode(mode)
    
    def _check_segment(self,segment):
        try:
            self._check_segment_index(segment)
            self.segments[segment].check()
        except KeyError:
            print("you must set the mode first for segment {}".format(segment))
        except TypeError:
            print("you must set the color first for segment {}".format(segment))
        except IndexError as e:
            print(e)



        
    def _check_segment_index(self,segment):
        if not self._vaild_segment_index(segment):
            raise IndexError("Segment is outside of lighbar range!")

    def _vaild_segment_index(self,segment):
        return segment < len(self.segments)

class LightBarSegement:

    VAILD_MODES = [
        "solid",
        "slide",
        "blink_fast",
        "blink_slow"
    ]

    def __init__(self,color=(None),mode=None):
        self.color = color
        self.mode = mode

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "{}:{}".format(
            re.findall('[^()]+',str(self.color))[0]
            ,self.mode)

    def set_mode(self,mode):
        self._check_mode(mode)
        self.mode = mode

    def set_color(self,color):
        self._check_color(color)
        self.color = color

    def check(self):
        self._check_mode(self.mode)
        self._check_color(self.color)

    def _check_mode(self,mode):
        if not self._vaild_mode(mode):
            raise KeyError("{} is an invaild mode!".format(mode))

    def _vaild_mode(self,mode):
        return mode in self.VAILD_MODES

    def _check_color(self,color):
        if not self._viald_color(color):
            raise TypeError("{} is an invaild color!".format(color))

    def _viald_color(self,color):
        return bool(re.match(r"\([0-9]+, [0-9]+, [0-9]+\)",str(color)))


