import datetime

title = input("どの時間を計算しますか？:")
time = int(input("1日に何時間取りたいですか？:"))

def cal():
    
ima = datetime.datetime.now()
end = datetime.datetime(2022,1,1,0,0,0)

plan = end - ima

print(plan)