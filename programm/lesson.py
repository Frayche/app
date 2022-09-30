file = open("test.txt")
file_with_lines = file.readlines()
for line in file_with_lines:
    a = line.split()
print("a =", a)
n = len(a)
for i in range(n-1):
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:                  # если порядок элементов пары неправильный
            a[j], a[j + 1] = a[j + 1], a[j]  # меняем элементы пары местами

print('Отсортированный список:', a)
