import numpy as np  

# a = np.arange(15).reshape(3, 5) #0-15까지 3*5행렬
# print(a)
# print(type(a))
# print(a.shape) #(3,5)
# print(a.ndim) #배열의 축수


# 1에서 10까지 값을 가지는 크기가 10인 1차원 배열 n_arr을 생성하여라. 이 배열이 메모리에서 차지하는 크기는 얼마인가? 다음의 밑줄 친 부분에 알맞은 코드를 입력하여 다음과 같이 바이트 단위로 출력하여라(힌트 : itemsize와 size 속성 값을 곱한다).
# n_arr=np.array(range(1,11),dtype='int32')
# print(n_arr)
# print(n_arr.itemsize)
# print(n_arr.size)
# data_size=n_arr.size*n_arr.itemsize
# print(data_size)
# p_num=np.random.rand(6) #난수생성

#사용자로부터 2이상의 수 n을 입력으로 받아서, 입력된 수를 바탕으로 다음과 같은 nxn 크기의 다차원 배열 a를 생성하는 프로그램을 작성하시오. 이 때 배열의 내용은 0과 1의 값이 체크 판 패턴으로 교차하여 나타나도록 하여라.
n=int(input('n을 입력하시오'))
#a=np.ones((n,n),dtype='int32') #1로 이루어진 정사각행렬
a=np.zeros((n,n),dtype='int32')
for i in range(n):
       for j in range(n):
              if (i+j)%2==0:
                     a[i,j]=1


print(a)




