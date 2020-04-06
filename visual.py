import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from bubble import bubble_sort
from insertion import insertion_sort_while
from merge import merge_sort, merge
from quicksort import quick_sort, partition, quicksort
from selection import selection
from maxheap import heap_sort
import sys


sys.setrecursionlimit(1500)

if __name__ == "__main__":
    N = int(input("Enter number of integers: "))
    choice_menu = "Enter sorting method:\n(b)ubble\n(h)eap\n(i)nsertion\n(m)erge \
        \n(q)uick\n(s)election\n"
    choice = input(choice_menu).strip().lower()

    A = [i + 1 for i in range(N)]
    random.seed(time.time())
    random.shuffle(A)

    if choice == "b":
        title = "Bubble sort"
        generator = bubble_sort(A)
    elif choice == "i":
        title = "Insertion sort"
        generator = insertion_sort_while(A)
    elif choice == "m":
        title = "Merge sort"
        generator = merge_sort(A, 0, N - 1)
    elif choice == "q":
        title = "Quick sort"
        generator = quicksort(A, 0, N - 1)
    elif choice == "h":
        title = "Maxheap sort"
        generator = heap_sort(A)
    else:
        title = "Selection sort"
        generator = selection(A)


    fig, ax = plt.subplots()
    ax.set_title(title)
    bar_rects = ax.bar(range(len(A)), A, align="edge")
    ax.set_xlim(0, N)
    ax.set_ylim(0, int(1.1 * N))
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)


    iteration = [0]
    def update_fig(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f"Number of operations: {iteration[0]}")

    anim = animation.FuncAnimation(fig, func=update_fig,
        fargs=(bar_rects, iteration), frames=generator, repeat=False, interval = 20,
        save_count= 200)
    plt.show()
    try:
        anim.save(f'gifs/{title}.gif', writer = 'imagemagick')
    except:
        pass
    print("COMPLETED!")

