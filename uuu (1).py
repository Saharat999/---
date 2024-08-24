oo = {}
ii = []
qq = []

while True:
    A = input('Date: ')
    if A == 'exit':
        kk = input('วันที่ที่เลือก: ')
        if kk in oo:
            kkk_list = oo[kk]
            for kkk in kkk_list:
                if kkk >= 0:
                    ii.append(kkk)
                elif kkk < 0:
                    qq.append(kkk)
            summ = sum(qq)
            sumn = sum(ii)
            print("สรุปรายรับรายจ่ายวันที่:", kk)
            print("รายจ่าย: ", summ)
            print("รายรับ: ", sumn)
        break
    else:
        K = input('Detail: ')
        j = int(input('Money: '))
        if A not in oo:
            oo[A] = []
        oo[A].append(j)
