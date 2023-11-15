import panel as pn

from myapp.sliders.sinewave import SineWave

def createApp():
    sw = SineWave()
    print(sw)
    return pn.Row(sw.param, sw.plot).servable()