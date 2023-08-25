for i in range(0, 220, 20):
    for j in range(1, 4):
        if i/100 == int(i/100):
            print(f"I={i/100:.0f} J={j+i/100:.0f}")
        else:
            print(f"I={i/100} J={j + i/100}")