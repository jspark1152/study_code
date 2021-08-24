#사전 자료형은 Key와 Value의 순서쌍 형태

data = dict()
#선언 시 data[ 키 ] = 값
data['사과']='Apple'
data['바나나']='Banana'
data['코코넛']='Coconut'

print(data)

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

#키 데이터만 뽑아서 리스트로 이용할 때 keys() 이용
#값 데이터만 뽑아서 리스트로 이용할 때 values() 이용

key_list=data.keys()
value_list=data.values()

print(key_list, value_list)

for i in key_list:
    print(data[i])