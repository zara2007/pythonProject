print("Choose your branch")
print("1-Science")
print("2-Human")
print("3-Art")
print("4-sport")
choose = int(input())
if choose ==1:
    print("1-Math")
    print("2-Physics")
    sub_choose = int(input())
    if sub_choose == 1:
        print("You're Financier")
    elif sub_choose == 2:
        print("Engineer")
    else:
        print("Please choose between 1 and 2")
if choose == 2:
    print("Вы выбрали humaniration subjects")
    print("1- history")
    print("2-foteign languages")
    sub_choose = int(input())
    if sub_choose == 1:
        print("historic")
    elif sub_choose==2:
        print("translater")
    else:
        print("please choose beetween 1 and 2")
if choose == 3:
    print("Вы выбрали art")
    print("1- drawing")
    print("2-singer")
    sub_choose = int(input())
    if sub_choose == 1:
        print("painter")
    elif sub_choose==2:
        print("singer")
    else:
        print("please choose beetween 1 and 2")
if choose == 4:
    print("sport")
    print("1- team")
    print("2-indvidual")
    sub_choose = int(input())
    if sub_choose == 1:
        print("footballer")
    elif sub_choose==2:
        print("boxer")
    else:
        print("please choose beetween 1 and 2")
