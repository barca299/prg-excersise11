import random

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


#def main():

if __name__ == "__main__":
    values = random_numbers(10)  # 10 čísel v rozsagit hu 0–100
    print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]

    small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20
    print(small)

    min_index = selection_sort(values)
    #main()

