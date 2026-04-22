import random, matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(values):

    for j in range(len(values)):
        min_indexy = j
        min_values = values[min_indexy]
        for i in range(j + 1, len(values)):
            if values[i] < min_values:
                min_indexy = i
                min_values = values[i]

        values[j], values[min_indexy] = values[min_indexy], values[j]
    print(values)
    return values

def bubble_sort(values):
    plt.ion()
    plt.show()
    for j in range(len(values)):
        for i in range(len(values) - j - 1):

            if values[i] > values[i + 1]:
                values[i], values[i+1] = values[i+1], values[i]
            index_highlight1 = i
            index_highlight2 = i + 1
            colors = ["steelblue"] * len(values)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(values)), values, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)
    plt.ioff()
    plt.show()
    print(values)
    return values

#def main():

if __name__ == "__main__":
    values = random_numbers(10)
    values_1 = random_numbers(10)
    # 10 čísel v rozsahu 0–100
    #print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]

    small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20
    #print(small)

    min_index = selection_sort(values)
    values_bubble = bubble_sort(values_1)
    #main()

