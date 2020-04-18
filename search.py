
#def binary_search(list_in: list[int], item: int) -> int:

def binary_search(list_in, item):
    """
    if item exits in list_in, this function returns its position in the list.
    :param list_in: list of integers
    :param item: integer to be searched in list_in
    :return: position of item in list_in
    """

    l = 0
    u = len(list_in) - 1

    while l <= u:
        mid = (l + u) // 2
        if list_in[mid] == item:
            return mid
        else:
            if list_in[mid] < item:
                l = mid + 1
            else:
                u = mid - 1

my_list = [2,89,46,10,34,99,23,67]
#my_item = 99
my_item = 11
item_pos = binary_search(my_list,my_item)

if item_pos is None:
    print("item not found")
else:
    print("position of the item is "+ str(item_pos + 1))






