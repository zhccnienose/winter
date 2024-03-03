# 查询第一个点击量比hits大的位置
def find_pos(list_hot, list_hot_hit, lside, rside, hits):
    for i in range(len(list_hot) - 1, -1, -1):
        if list_hot_hit[i] < hits <= list_hot_hit[i+1]:
            # print(list_hot[i], list_hot_hit[i], "after")
            return list_hot[i+1], list_hot_hit[i+1]

    # print(list_hot[0], list_hot_hit[0], "before")
    return list_hot[0], list_hot_hit[0]
