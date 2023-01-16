# 2563 색종이 

white_line = [0 for _ in range(100)]


white_plate = []

for _ in range(100) :
    white_plate.append(white_line)  ## 100 x 100 흰색판을 깔고 시작.

# n = int(input())

for i in range(3,13):
    for j in range(3,13):
        white_plate[i][j] = 1
print(white_plate[:5])




# for _ in range(n):
#     xstart,ystart = map(int,input().split())

#     for y in range(ystart,ystart+10):
#         for x in range(xstart,xstart+10):
#             white_plate[x][y] = 1


# # 칠해지는 곳 1칸마다 넓이 1을 표시 

# result = 0 

# print(white_plate[3][7])


# # 전체 판의 칠해져있는 넓이를 다 더하면.

# for i in range(100) :
#     result += sum(white_plate[i])

# print(result)