#coding=gbk
#����001
"""
��Ŀ�� ��1��2��3��4�����֣�����ɶ��ٸ�������ͬ����
#�ظ����ֵ���λ�������Ƕ��١�
"""

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=k) and (i!=j) and (j!=k):
               print i,j,k

