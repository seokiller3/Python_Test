names = ["Alice", "Bob", "Charlie"]
bets = [100, 150, 200]
bonuses = ["10.25%", "5.50%", "8.75%"]

result_dict = {name: bet * (1 + float(bonus.strip('%')) / 100) for name, bet, bonus in zip(names, bets, bonuses)}
print(result_dict)
