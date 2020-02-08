""" This Program for Internship 2020"""
def main():
    list_hangman = input().split(" ")
    list_result = []
    score = 0
    list_predict = []
    un_list = []
    for _ in range(5):
        list_predict.append(input())
    for _ in range(12):
        list_result.append("_")
    for j in range(6):
        undefine = 0
        if(j == 0):
            for i in range(12):
                if(i < 11):
                    print(list_result[i], end=" ")
                else:
                    print(list_result[i])
        else:
            for i in list_hangman:
                if(list_predict[j-1] == i and list_hangman.index(i) < len(list_result)-1):
                    list_result[list_hangman.index(i)] = list_predict[j-1]
                    score += 1
                    print(list_result[list_hangman.index(i)], end=" ")
                elif(list_predict[j-1] == i and list_hangman.index(i) > len(list_result)-1):
                    list_result[list_hangman.index(i)] = list_predict[j-1]
                    score += 1
                    print(list_result[list_hangman.index(i)])
                else:
                    if(list_hangman.index(i) < len(list_result)-1):
                        undefine += 1
                        print(list_result[list_hangman.index(i)], end=" ")
                    elif(list_hangman.index(i) > len(list_result)-1):
                        undefine += 1
                        print(list_result[list_hangman.index(i)])
                    if(undefine == 12):
                        un_list.append(list_predict[j-1])
            for k in un_list:
                if(un_list.index(k)+1 == len(un_list)):
                    print(k, end=" ")
                else:
                    print(k, end=" ")
            print("")
    print(score)

main()