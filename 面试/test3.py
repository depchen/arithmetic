
# singer_周杰伦|周;song_冰雨|gggg|g;actor_周杰伦
# 周的g
# 周/singe的g/song
if __name__ == '__main__':
    s1=input()
    s2=input()
    ss2=[-1]*len(s2)
    ss3=[-1]*len(s2)
    s1=s1.split(';')
    ss1=[]
    if s1==None or s2==None:
        print('')
    for i in range(len(s1)):
        a=s1[i].split('|')
        a[0]=a[0].split('_')[1]
        ss1.append(a)
    for i in range(len(ss1)):
        for j in range(len(ss1[i])):
            if ss1[i][j] in s2:
                aa=s2.find(ss1[i][j])
                if ss2[s2.find(ss1[i][j])]==-1:
                    ss2[s2.find(ss1[i][j])] = i+2
                    ss3[s2.find(ss1[i][j])] = len(ss1[i][j])
                elif ss2[s2.find(ss1[i][j])]==i+2:
                    if ss3[s2.find(ss1[i][j])] < len(ss1[i][j]):
                        ss2[s2.find(ss1[i][j])] = i+2
                        ss3[s2.find(ss1[i][j])] = len(ss1[i][j])
                else:#2,3,4
                    if ss3[s2.find(ss1[i][j])] < len(ss1[i][j]):
                        ss2[s2.find(ss1[i][j])] = i+2
                        ss3[s2.find(ss1[i][j])] = len(ss1[i][j])
                    elif ss3[s2.find(ss1[i][j])] == len(ss1[i][j]):
                        ss2[s2.find(ss1[i][j])] = ss2[s2.find(ss1[i][j])] + i + 2
    i=0
    a=ss2[i]
    while(a):
        if ss2[i] == 2:
            s2=s2[:i+ss3[i]]+"/singe"+s2[i+ss3[i]:]
            ss2 = ss2[:i+ss3[i]]+[-1]*6+ss2[i+ss3[i]:]
            ss3 = ss3[:i+ss3[i]]+[-1]*6+ss3[i+ss3[i]:]
            a=ss2[i]
            i = i + 1
        elif ss2[i] == 3:
            s2 = s2[:i + ss3[i]] + "/song" + s2[i + ss3[i]:]
            ss2 = ss2[:i + ss3[i]] + [-1] * 5 + ss2[i + ss3[i]:]
            ss3 = ss3[:i + ss3[i]] + [-1] * 5 + ss3[i + ss3[i]:]
            a = ss2[i]
            i = i + 1
        elif ss2[i] == 4:
            s2 = s2[:i + ss3[i]] + "/actor" + s2[i + ss3[i]:]
            ss2 = ss2[:i + ss3[i]] + [-1] * 6 + ss2[i + ss3[i]:]
            ss3 = ss3[:i + ss3[i]] + [-1] * 6 + ss3[i + ss3[i]:]
            a = ss2[i]
            i = i + 1
        elif ss2[i] == 6:
            s2 = s2[:i + ss3[i]] + "/singe,actor" + s2[i + ss3[i]:]
            ss2 = ss2[:i + ss3[i]] + [-1] * 12 + ss2[i + ss3[i]:]
            ss3 = ss3[:i + ss3[i]] + [-1] * 12 + ss3[i + ss3[i]:]
            a = ss2[i]
            i = i + 1
        elif ss2[i] == 7:
            s2 = s2[:i + ss3[i]] + "/song,actor" + s2[i + ss3[i]:]
            ss2 = ss2[:i + ss3[i]] + [-1] * 11 + ss2[i + ss3[i]:]
            ss3 = ss3[:i + ss3[i]] + [-1] * 11 + ss3[i + ss3[i]:]
            a = ss2[i]
            i = i + 1
        elif ss2[i] == 9:
            s2 = s2[:i + ss3[i]] + "/singe,song,actor" + s2[i + ss3[i]:]
            ss2 = ss2[:i + ss3[i]] + [-1] * 17 + ss2[i + ss3[i]:]
            ss3 = ss3[:i + ss3[i]] + [-1] * 17 + ss3[i + ss3[i]:]
            a = ss2[i]
            i = i + 1
        else:
            if i+1>=len(ss2):
                a=None
            else:
                a=ss2[i]
            i = i + 1

    print(s2)




