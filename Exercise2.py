import random

# 1a. Tìm số lớn nhất trong list


def find_max_num(num_list, k):
    final_list = []
    for i in range(len(num_list) - k + 1):
        max_result = max(num_list[i:k + i])
        print(
            f"Lượt thứ {i + 1} list {num_list[i:k + i]} phần tử max là: {max_result}")
        final_list.append(max_result)
    print(f"List bao gồm phần tử max: {final_list}")


num_list_a = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k_a = 3
find_max_num(num_list_a, k_a)


# 1b. Tìm số lớn nhất trong list nhỏ
def find_max_in_sublist(num_list, k):
    sub_list = []
    final_list = []
    for element in num_list:
        sub_list.append(element)
        if len(sub_list) == k:
            del sub_list[0]
            max_result = max(sub_list)
            print(f"list {sub_list} phần tử max là: {max_result}")
            final_list.append(max_result)
    print(f"List bao gồm phần tử max: {final_list}")


num_list_b = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k_b = 4
find_max_in_sublist(num_list_b, k_b)


# 2. Viết function trả về một dictionary đếm số lượng chữ xuất hiện trong một từ
def count_char(string):
    dict_count_chars = {}
    for i in string:
        if i in dict_count_chars:
            dict_count_chars[i] += 1
        else:
            dict_count_chars[i] = 1
    return dict_count_chars


print(count_char("Happiness"))


def count_chars(string):
    dict_count_chars = {}
    for char in string:
        if char not in dict_count_chars:
            dict_count_chars[char] = string.count(char)
    return dict_count_chars


print(count_chars("smiles"))


# 3. Viết function đọc các câu trong một file txt
def count_word_in_file(file_path):
    with open(file_path, 'r') as file:
        dict_count_word = {}
        contents = file.read().lower()
        contents = contents.replace('.', '')
        words = contents.split()
        for word in words:
            if word not in dict_count_word:
                dict_count_word[word] = 1
            else:
                dict_count_word[word] += 1
        return dict_count_word


file_path = "P1_data.txt"
print(count_word_in_file(file_path))


# 4. Viết chương trình tính khoảng cách chỉnh sửa tối thiểu Levenshtein
def edit_distance(source, target):
    distance = []
    for idx in range(len(source) + 1):
        row = [0] * (len(target) + 1)
        distance.append(row)

    for idx in range(len(source) + 1):
        distance[idx][0] = idx
    for idx in range(len(target) + 1):
        distance[0][idx] = idx

    for idx in range(1, len(source) + 1):
        for jdx in range(1, len(target) + 1):
            if source[idx - 1] == target[jdx - 1]:
                distance[idx][jdx] = distance[idx - 1][jdx - 1]
            else:
                del_cost = distance[idx - 1][jdx] + 1
                ins_cost = distance[idx][jdx - 1] + 1
                sub_cost = distance[idx - 1][jdx - 1] + 1
                distance[idx][jdx] = min(del_cost, ins_cost, sub_cost)

    return distance[len(source)][len(target)]


source = 'halo'
target = 'hello'
print(
    f"Khoảng cách chỉnh sửa tối thiểu giữa '{source}' và '{target}' là {edit_distance(source, target)}")
