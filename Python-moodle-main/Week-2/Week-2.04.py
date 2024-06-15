



deposit = float(input())
interest_rate = 0.04
for year in range(1, 4):
    balance = deposit * (1 + interest_rate) ** year
    print(f"Balance as of end of Year {year}: ${balance:.2f}.")
