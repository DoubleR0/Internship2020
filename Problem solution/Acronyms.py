""" This Program for Internship 2020"""
def main():
    list_sorting = []
    for i in range(int(input())):
        list_sorting.append(FindUpper(input()))
    list_sorted = SortLen(sorted(list_sorting))
    print(list_sorted)

def FindUpper(sentence):
    word = ""
    for i in sentence:
        if i.isupper():
            word += i
    return word

def SortLen(list_sorting):
    for i in range(len(list_sorting)):
        for j in range(len(list_sorting)-1):
            if len(list_sorting[j]) < len(list_sorting[j+1]):
                list_sorting[j], list_sorting[j+1] = list_sorting[j+1], list_sorting[j]
    return list_sorting
main()