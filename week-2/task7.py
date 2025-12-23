from collections import Counter

def shop(purchases_str):
    items = purchases_str.split()
    counter = Counter(items)
    
    print("Количество продуктов:")
    for item in sorted(counter):
        print(f"{item}: {counter[item]}")
    
    if counter:
        popular = counter.most_common(1)[0][0]
        print(f"\nСамое популярное: {popular}")
    
    once = [item for item, count in counter.items() if count == 1]
    print(f"\n1 раз выбрано: {' '.join(once)}")
    
    print("\nОтсортировано по убыванию:")
    for item, count in counter.most_common():
        print(f"{item} {count}")



purchases = input(":")
shop(purchases)
