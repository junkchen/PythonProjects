movies = ["The Holy Grail", "The Life of Brain", "The meaning of Life"]
print(movies[1])

cast = ["Cleese", 'Plain', 'Jones', "Idle"]
print(cast)
print(len(cast))
print(cast[1])

# add date item
cast.append("Gilliam")
print(cast)

# delete last data item
cast.pop()
print(cast)

# 在列表末尾增加一个数据项集合
cast.extend(["Gilliam", "Chapman"])
print(cast)

# 删除指定的数据
cast.remove("Chapman")
print(cast)

# 在指定为添加数据
cast.insert(0, "Chapman")
print(cast)

movies.insert(1, 1975)
movies.insert(3, 1979)
movies.insert(5, 1983)
print(movies)

fav_movies = ["The Holy Grail", "The Life of Brain"]
print(fav_movies[0])
print(fav_movies[1])

for each_flick in fav_movies:
    print(each_flick)

count = 0
while count < len(movies):
    print(movies[count])
    count = count + 1

movies = [
    "The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
    ["Graham Chapman",
        ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
print(movies[4][1][3])
print(movies)

for each_item in movies:
    print(each_item)

for each_item in movies:
    if isinstance(each_item, list):
        for sub_item in each_item:
            print(sub_item)
    else:
        print(each_item)


def iterate_element(item):
    if isinstance(item, list):
        for nested_item in item:
            iterate_element(nested_item)
    else:
        print(item)


iterate_element(movies)


def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)


print_lol(movies)
