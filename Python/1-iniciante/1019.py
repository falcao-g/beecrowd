seconds = int(input())
times = [3600, 60, 1]

converted = []
for time in times:
    converted.append(int(seconds / time))
    seconds -= int(seconds/time) * time
    
print(f"{converted[0]}:{converted[1]}:{converted[2]}")