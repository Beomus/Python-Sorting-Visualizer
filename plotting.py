import matplotlib.pyplot as plt
from matplotlib import animation as animation

import random
import time


A = [x + 1 for x in range(100)]
random.shuffle(A)


def generator(arr):
	for _ in range(100):
		random.shuffle(arr)
		yield arr


fig, ax = plt.subplots()

ax.set_title("Graph")
bar_rects = ax.bar(range(len(A)), A, align="edge")
ax.set_xlim(0, 100)
ax.set_ylim(0, int(1.07 * 100))

text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

iteration = [0]
gen = generator(A)

def update_fig(arr, rects, iteration):
	for rect, val in zip(rects, arr):
		rect = rect.set_height(val)
	iteration[0] += 1
	text.set_text(f"Iteration: {iteration[0]}")

anim = animation.FuncAnimation(fig, func=update_fig, fargs=(bar_rects, iteration), frames=gen, repeat=False)
plt.show()
print("Finished.")
