larg= int(input("Digite a largura: "))
alt= int(input("Digite a altura: "))
tag= "#"

def hashtag():
    print(tag * larg)
    for i in range(alt-2):
        print(tag + (' '*(larg-2)) + tag)
    print(tag * larg)

hashtag()