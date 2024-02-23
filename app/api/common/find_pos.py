# 查询第一个hit比hits小的位置
def find_pos(list_hot, list_hot_hit, lside, rside, hits):
    if lside > rside:
        hot_value = list_hot[rside].decode("utf-8")
        value = list_hot_hit[rside]
        print("-----------", hot_value, value)
        return hot_value, value

    mid = (lside + rside) // 2

    if list_hot_hit[mid] >= hits:
        return find_pos(list_hot, list_hot_hit, lside, mid - 1, hits)
    else:
        return find_pos(list_hot, list_hot_hit, mid + 1, rside, hits)
