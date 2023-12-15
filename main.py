def combinations_function(m, n):
    """
        定義：算出m個index中取出n個的組合
    """
    if n > m or m < 4:
        return

    # default values
    total_index = list(range(m))  # 全部的index
    stop_idx_location = -2  # 倒數第幾個index,從這index往前都是停止的
    result = list(range(n))  # 第一個結果
    last_idx = result[-1]  # 最後一個index初始值
    current_times = 1  # 執行第幾個結果

    # print(result)

    while True:
        if last_idx < m - 1:
            # 如果最後一個欄位還能向後移動，則移動
            last_idx += 1
            result = result[0:-1]
            result.append(last_idx)
        else:
            # 最後一個欄位已經到最後一個index

            if result[stop_idx_location:] == total_index[stop_idx_location:]:
                # 固定點後面已經沒有其他組合 or 最後一種組合
                if result[0] == m - n:
                    # 最後一種組合
                    print('combinations_function 有', current_times, '種結果')
                    return
                else:
                    stop_idx_location -= 1  # 固定點往前
                    result[stop_idx_location] += 1  # 固定點index值加一
                    # 前面有index+1，後方的index(共stop_idx_location*-1-1個)回來緊貼著變動的index
                    for i in reversed(range(1, -stop_idx_location)):
                        result[-i] = result[-i - 1] + 1

            else:
                for j in range(2, -stop_idx_location + 1):
                    # 由後往前確認是否有空隙
                    if result[-j] + 1 == result[-j + 1]:
                        pass
                    else:
                        result[-j] += 1
                        for k in reversed(range(1, j)):
                            result[-k] = result[-k - 1] + 1

                        break  # 停止檢查

        last_idx = result[-1]
        current_times += 1
        # print(result, current_times)


def combinations_package(m, n):
    """
        使用套件
    """
    from itertools import combinations
    news_combinations_list = list(combinations(range(m), n))
    print('combinations_package 有', len(news_combinations_list), '種結果')


if __name__ == '__main__':
    # 自己寫的程式
    combinations_function(16, 4)

    # 使用套件
    combinations_package(16, 4)
