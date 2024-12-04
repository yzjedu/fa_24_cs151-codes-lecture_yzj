def read_file_to_table(filename):
    all_years = []  # start with empty list
    try:
        file = open(filename, "r")
        for line in file:
            data = line.split()
            all_years.append(data)
        file.close()
    except:
        print("File doesn’t exist")
    return all_years  # can return because it exists whether or not excpetion happened


# find an actress by year using linear search
def find_by_year_linear(actresses, year):
    count = 0
    for a in actresses:
        count += 1
        if a[0] == str(year):
            print(count)
            return a
    return "OOPS"


# Print out each part of a single actress's data
def print_out_actress(actress):
    for item in actress:
        print(item)


def find_by_year_binary(my_list, target):
    startIndex = 0  # first index of portion we’re examining
    endIndex = len(my_list) - 1  # last index of portion we’re examining
    count = 0
    while endIndex >= startIndex:  # we haven’t run out of places to look
        middle = (startIndex + endIndex) // 2  # index of element in middle to check
        count += 1
        this_actress_year = my_list[middle][0]  # the one we are looking at right now

        if this_actress_year == target:
            print(count)
            return middle  # target found at middle—so bail out
        elif this_actress_year > target:
            endIndex = middle - 1  # search left half of array
        else:
            startIndex = middle + 1  # search right half  of array

    return -1  # if we reached this line….


def main():
    data = read_file_to_table("actress.txt")

    year = input(
        f"From what year do you want to know the best actress? ({data[0][0]}-{data[-1][0]}) "
    )

    print("Let's try linear search")
    actress = find_by_year_linear(data, year)
    print_out_actress(actress)

    print("\nNow let's try binary search")
    index = find_by_year_binary(data, year)
    actress = data[index]
    print_out_actress(actress)


main()
