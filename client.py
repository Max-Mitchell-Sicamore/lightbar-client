import re
class LightBarCleint:

    def __init__(self,size):
        self.segments = list(
            map(lambda x:LightBarSegement() ,([None]*size))
        )


    def set_segment(self,segment,color,mode):
        self._check_segment(segment)
        self.segments[segment].set_color(color)
        self.segments[segment].set_mode(mode)
        
    def _check_segment(self,segment):
        if not self._vaild_segment(segment):
            raise "Segment is outside of lighbar range!"

    def _vaild_segment(self,segment):
        return segment < len(self.segments)

class LightBarSegement:

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
        self.mode = mode

    def set_color(self,color):
        self.color = color

# tests 
# l = LightBarCleint(4)
# l.set_segment(0,(255,20,10),"blink")
# print(
#     l.segments
)