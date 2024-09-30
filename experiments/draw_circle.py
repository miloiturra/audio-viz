import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from typing import Any

fig, ax = plt.subplots()
circle = Circle((0.5, 0.5), 0.1, color='blue', fill=False)
ax.add_patch(circle)
ax.set_aspect('equal', 'box')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Remove axis ticks, labels, and frames
ax.set_xticks([])
ax.set_yticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.ion()

background = fig.canvas.copy_from_bbox(ax.bbox)

def audio_callback(indata: np.ndarray, frames: int, time: Any, status: Any) -> None:
    amplitude = np.linalg.norm(indata) / np.sqrt(len(indata))
    circle.set_radius(amplitude * 0.5 + 0.01)
    fig.canvas.restore_region(background)
    ax.draw_artist(circle)
    fig.canvas.blit(ax.bbox)

def start_stream() -> None:
    with sd.InputStream(callback=audio_callback):
        plt.show(block=True)

start_stream()
