# モジュールのインポート
import numpy as np
import matplotlib.pyplot as plt

def plot_array_with(array,time,isContinue = True): # 配列 array の先頭から n 番目 までを時間ごとに更新していく
    for i in range(len(array)- 1):
        plt.plot(array[:i])
        plt.draw()
        plt.pause(time)
        plt.cla()
    if(isContinue): # 描画を残す場合
        plt.plot(array)
        plt.show()
    else:           # 描画を残さない場合
        plt.draw()
        plt.pause(time)
    return None

def main(m,n,Range = 1):
    a = np.random.rand(m) # 長さ m の 0 ~ 1 の数字によるnp.array

    a -= 0.5
    a *= Range

    # 今までの総和を配列に記録する
    acc = n
    lst = [n]
    for i in range(m):
        acc += a[i]
        lst.append(acc)

    plot_array_with(lst,0.5)
    return None

main(30, 10)
