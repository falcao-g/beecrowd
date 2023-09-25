estrada, dist_pedagios = map(int, input().split())
custo_km, custo_pedagio = map(int, input().split())

num_pedagios = estrada // dist_pedagios

custo_total = (num_pedagios * custo_pedagio) + (estrada * custo_km)

print(custo_total)