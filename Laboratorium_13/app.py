from typing import List

def sorting(list: List[str]) -> List[str]:
    for x in range(len(list)): #Aby algorytm zadziałał, należy wykonać tyle razy ile jest elementów listy
        for y in range(len(list)-1): #Algorytm przechodzi po całej liście, -1 jest z powodu sprawdzania elemnót o 1 indeks w przód
            if(len(list[y])>len(list[y+1])): #algorytm sortuje po długości wyrazów, stąd element len
                pom = list[y] #algorytm bąbelkowy, elementy przy każdej iteracji porószają się o jedno miejsce
                list[y] = list[y+1]
                list[y+1] = pom
            
    return list
