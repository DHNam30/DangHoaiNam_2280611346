def dao_nguoc_List(lst):
    return lst[::-1]
input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

list_dao_nguoc = dao_nguoc_List(numbers)
print("List sau khi đảo ngược:", list_dao_nguoc)