#!/usr/bin/env python
# coding:utf-8
import sys
from PIL import Image
import numpy as np
np.save('pixel',
	np.vstack(
		{
			tuple(row)
			for row in np.vstack(
				np.array(
					Image.open(f).convert('RGB')
				).reshape((-1,3))
				for f in sys.argv[1:]
			)
		}
	)
)
