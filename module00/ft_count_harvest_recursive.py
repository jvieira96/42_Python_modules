def ft_count_harvest_recursive():
    def count(n):
        if n > 0:
            count(n - 1)
            print("Day ", n)
    days = int(input("Days until harvest: "))
    count(days)
    print("Harvest time!")