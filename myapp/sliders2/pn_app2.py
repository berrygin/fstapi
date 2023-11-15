import panel as pn

from myapp.sliders2.sinewave2 import SineWave2

def createApp2():
    sw = SineWave2()
    return pn.Row(sw.param, sw.plot).servable()