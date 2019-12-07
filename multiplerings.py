import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import animation
import os

# It should be the path of ffmpeg.exe
matplotlib.rcParams['animation.ffmpeg_path'] = 'C:\\Users\\jyh\\Downloads\\ffmpeg-20190930-6ca3d34-win64-static\\ffmpeg-20190930-6ca3d34' \
                                 '-win64-static\\bin\\ffmpeg.exe '

# New figure with white background
fig = plt.figure(figsize=(6, 6), facecolor='white')

# New axis over the whole figureand a 1:1 aspect ratio
ax = fig.add_axes([0.005, 0.005, 0.990, 0.990], frameon=True, aspect=1)

# Number of ring
n = 100
size_min = 30
size_max = 50 * 800

# Ring position
P = np.ones((70, 2))*0.5

# Ring colors
C = np.ones((n, 4)) * (0, 1, 0, 1)

# C = np.ones((n,3)) * (1,0,1)
# Alpha color channel goes from 0 (transparent) to 1 (opaque)
C[:, 2] = np.linspace(0, 1, n)

# Ring sizes
S = np.linspace(size_min, size_max, n)

# Scatter plot
ax.text(0.5, 0.8, 'breathe with the expansion of waves', style='italic', horizontalalignment='center')
scat = ax.scatter(P[:, 0], P[:, 1], s=S, lw=0.5,
                  edgecolors=C, facecolors='None')

# Ensure limits are [0,1] and remove ticks
ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_ylim(0, 1), ax.set_yticks([])


def update(frame):
    global P, C, S

    C[:, 3] = np.maximum(0, C[:, 3] - 1.0 / n)

    S += (size_max - size_min) / n

    # Reset ring specific ring (relative to frame number)
    i = frame % 50
    P[i] = np.array([0.5,0.5])
    S[i] = size_min
    C[i, 3] = 1

    # Update scatter object
    scat.set_edgecolors(C)
    scat.set_sizes(S)
    scat.set_offsets(P)
    return scat,


animate = FuncAnimation(fig, update, frames=600, interval=70)

FFwriter = animation.FFMpegWriter(fps=10)

animate.save('bigideaslab_1_min.mp4', writer=FFwriter, dpi=360)
plt.show()
