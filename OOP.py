
class Instrument:
    def play(self):
        print("Instrument is playing music")

class Guitar(Instrument):
    def string_sound(self):
        print("Guitar produces string sound")

class Piano(Instrument):
    def key_sound(self):
        print("Piano produces key sound")

g = Guitar()
p = Piano()

g.play()
g.string_sound()

p.play()
p.key_sound()
