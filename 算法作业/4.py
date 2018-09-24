#实现棋盘覆盖算法
#输入：rx=0,ry=0,sx=4,sy=8,size=16
#(rx，xy为棋盘初始坐标;sx,sy为特殊方格的坐标;size为棋盘大小)
#输出：
#31  31  32  32  36  36  37  37  10  10  11  11  15  15  16  16
#31  29  29  32  36  34  34  37  10  8   8   11  15  13  13  16
#33  29  30  30  35  35  34  38  12  8   9   9   14  14  13  17
#33  33  30  23  23  35  38  38  12  12  9   2   2   14  17  17
#41  41  40  23  26  26  27  27  -1  4   5   5   2   19  20  20
#41  39  40  40  26  24  24  27  4   4   3   5   19  19  18  20
#42  39  39  43  28  24  25  25  6   3   3   7   21  18  18  22
#42  42  43  43  28  28  25  1   6   6   7   7   21  21  22  22
#52  52  53  53  47  47  46  1   1   67  68  68  73  73  74  74
#52  50  50  53  47  45  46  46  67  67  66  68  73  71  71  74
#54  50  51  51  48  45  45  49  69  66  66  70  72  72  71  75
#54  54  51  44  48  48  49  49  69  69  70  70  65  72  75  75
#57  57  56  44  44  61  62  62  78  78  77  65  65  82  83  83
#57  55  56  56  61  61  60  62  78  76  77  77  82  82  81  83
#58  55  55  59  63  60  60  64  79  76  76  80  84  81  81  85
#58  58  59  59  63  63  64  64  79  79  80  80  84  84  85  85
def chess(rx,ry,sx,sy,size):
    global table
    global count
    if size == 1: #终止条件
        return
    half=size//2  #整体大小
    if sx<rx+half and sy<ry+half:  #特殊方块在 左上的情况
        count = count + 1  #L型骨牌数加1
        a=count #保存L骨牌数量
        chess(rx,ry,sx,sy,half)  #左上部分直接递归，其余每个部分需要设置特殊方块
        table[rx+half-1][ry+half]=a  #右上部分设置特殊方块
        chess(rx,ry+half,rx+half-1,ry+half,half) #右上部分递归
        table[rx + half][ry + half - 1] = a #左下部分设置特殊方块
        chess(rx+ half,ry , rx + half, ry + half - 1, half) #左下部分递归
        table[rx + half][ry + half] = a  #右下部分设置特殊方块
        chess(rx + half, ry + half, rx + half, ry + half, half) #右下部分递归
    elif sx>=rx+half and sy>=ry+half:  #特殊方块在 右下的情况
        count = count + 1
        a=count
        chess(rx+half, ry+half, sx, sy, half)
        table[rx + half - 1][ry + half-1] = a
        chess(rx, ry, rx + half - 1, ry + half-1, half)
        table[rx + half-1][ry + half] = a
        chess(rx , ry+ half, rx + half-1, ry + half, half)
        table[rx + half][ry + half-1] = a
        chess(rx + half, ry, rx + half, ry + half-1, half)
    elif sx>=rx+half and sy<ry+half:   #特殊方块在 左下的情况
        count = count + 1
        a=count
        chess(rx+half, ry, sx, sy, half)
        table[rx + half - 1][ry + half - 1] = a
        chess(rx , ry ,rx + half - 1, ry + half - 1, half)
        table[rx + half - 1][ry + half] = a
        chess(rx, ry + half, rx + half - 1, ry + half, half)
        table[rx + half][ry + half] = a
        chess(rx + half, ry + half, rx + half, ry + half, half)
    elif sx<rx+half and sy>=ry+half:  #特殊方块在 右上的情况
        count = count + 1
        a=count
        chess(rx, ry+half, sx, sy, half)
        table[rx + half - 1][ry + half - 1] = a
        chess(rx, ry, rx + half - 1, ry + half - 1, half)
        table[rx + half][ry + half - 1] = a
        chess(rx + half, ry, rx + half, ry + half - 1, half)
        table[rx + half][ry + half] = a
        chess(rx + half, ry + half, rx + half, ry + half, half)
#输出
def show(table):
    n = len(table)
    for i in range(n):
        for j in range(n):
            print("%-3d"%table[i][j], end=' ')
        print('')
#主函数
if __name__ == '__main__':
    count=0
    n=16
    table=[[-1 for x in range(n)] for i in range(n)]
    chess(0,0,4,8,n)
    show(table)