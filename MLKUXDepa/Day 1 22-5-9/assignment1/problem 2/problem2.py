
count = 0
m = -1
while True:
    build = int(input())
    if build == -1:
        break
    if m < build:
        m = build
        count += 1
print(count)