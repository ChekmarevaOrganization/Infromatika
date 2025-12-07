def read_purchases(path):
    purchases = []
    nopurchases = []
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = line.split(';')
            if len(parts) != 5:
                nopurchases.append(line)
                continue

            date = parts[0].strip()
            category = parts[1].strip()
            name = parts[2].strip()
            price_str = parts[3].strip()
            qty_str = parts[4].strip()

            if not price_str or not qty_str:
                nopurchases.append(line)
                continue

            try:
                price = float(price_str)
                qty = float(qty_str)
            except ValueError:
                nopurchases.append(line)
                continue

            if price < 0 or qty < 0:
                nopurchases.append(line)
                continue

            purchase = {
                "date": date,
                "category": category,
                "name": name,
                "price": price,
                "qty": qty,
            }
            purchases.append(purchase)

    return purchases, nopurchases


valid, invalid = read_purchases('purchases.txt')
print(valid)
print(invalid)

def count_errors(path):
    k = 0
    for i in path:
        if len(i) == 0:
            k+=1
    print(k)
    return k
def total_spent(purchases):
    total = 0.0
    for p in purchases:
        total += p["price"] * p["qty"]
    return total


def spent_by_category(purchases):
    cat = {
        "food": 0,
        "home": 0,
        "transport": 0,
        "other": 0,
        "health": 0,
        "entertainment": 0
    }
    for item in purchases:
        category = item["category"]
        price = item["price"]
        qty = item["qty"]
        total = price * qty

        if category in cat:
            cat[category] = cat[category] + total
        else:
            cat["other"] = cat["other"] + total

    return cat


def top_n_expensive(purchases, n=3):
    costs = []
    for p in purchases:
        costs.append(p["price"] * p["qty"])
    costs.sort(reverse=True)
    return costs[:n]


def write_report(purchases, errors, out_path):
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(f"всего_строк:{len(purchases) + len(errors)}\n")
        f.write(f"правильных:{len(purchases)}\n")
        f.write(f"ошибок:{len(errors)}\n")
        total = total_spent(purchases)
        f.write(f"общая_сумма:{total:.2f}\n")
        cats = spent_by_category(purchases)
        for cat, amount in cats.items():
            if amount > 0:
                f.write(f"{cat}:{amount:.2f}\n")
        top = top_n_expensive(purchases, 3)
        for i, cost in enumerate(top, 1):
            f.write(f"топ{i}:{cost:.2f}\n")



