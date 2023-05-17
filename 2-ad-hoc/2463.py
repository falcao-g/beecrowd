def max_sum(arr):
    resp = 0
    maior = 0

    for i in range(len(arr)):
        maior = max(0, maior+arr[i])

        resp = max(resp, maior)

    return resp

input()
print(max_sum([int(x) for x in input().split()]))