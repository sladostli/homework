class Sort:
    list = []

    def __init__(self, list):
        self.list = list
        pass

    def bubble(self, list):
        i = 0
        n = len(list)
        while i < n - 1:
            j = 0
            while j < n - 1 - i:
                if list[j] > list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
                j += 1
            i += 1
        return list

srt = Sort

while True:
    l = list(map(int, input('Введите список чисел\n').split()))
    print(srt.bubble(srt, l))
    