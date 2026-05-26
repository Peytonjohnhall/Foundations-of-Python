colors = ['red', 'green', 'blue', 'yellow']
for item in colors:
    tab_count = colors.index(item)
    index = colors.index(item)
    while True:
        print("\t" * tab_count, item)
        print("\t" * tab_count, "1")
        print("\t" * tab_count, "2")
        print("\t" * tab_count, "3")
        break
    if index > 3:
        break