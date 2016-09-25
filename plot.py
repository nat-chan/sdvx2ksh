import sys
import numpy as np
import libsixel
from libsixel.encoder import Encoder, SIXEL_OPTFLAG_WIDTH, SIXEL_OPTFLAG_COLORS
import matplotlib.pyplot as plt
from cStringIO import StringIO

encoder = Encoder()

def plot(fig):
#	fig.canvas.draw()
	w,h = fig.canvas.get_width_height()
	src = fig.canvas.tostring_rgb()
	encoder.encode_bytes(src, w, h, 3, None)

if __name__ == '__main__':
	X = np.arange(-3,3,0.1)
	Y = np.arange(-3,3,0.1)
	Z = np.cos(X) + np.sin(Y)
