def data_sort(data):
    return sorted(data)


input_data = list(set(input().lower().split()))

with open("sorted.txt", "a") as sorted_file:
    for word in data_sort(input_data):
        sorted_file.write(word)
        sorted_file.write("\n")

