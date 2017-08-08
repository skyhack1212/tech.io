def count_all_stars(galaxies):
    total_stars = 0
    for stars in galaxies:
        total_stars += stars  # fix me!
    return total_stars

#上面的方法其实等同于sum函数
galaxies = [37, 3, 2]
total_stars = sum(galaxies)
