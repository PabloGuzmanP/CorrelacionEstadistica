x = [3,5,2,4,9,8,6,5,7,4]
y = [5,7,1,6,15,10,7,5,6,9]

def mediaX():
    suma = 0
    for i in x:
        suma = suma + i
    media =suma/len(x)
    return (media)

def mediaY():
    suma = 0
    for i in y:
        suma = suma + i
    media = suma/len(y)
    return (media)

def covarianza():
    suma = 0
    for i in range (len(x)):
        suma = suma + ((x[i]-mediaX()) * (y[i]-mediaY()))
    cov = suma / len(x)
    return cov

def varianzaX():
    suma = 0
    for i in range (len(x)):
        suma = suma + ((x[i]-mediaX())**2)
    var = suma / len(x)
    return var

def varianzaY():
    suma = 0
    for i in range (len(y)):
        suma = suma + ((y[i]-mediaY())**2)
    var = suma / len(y)
    return var

def pearson():
    p=covarianza()/(varianzaX()*varianzaY())**0.5
    return p

if __name__ == '__main__':
    print("La media del arreglo X es: ", mediaX())
    print("La media del arreglo Y es: ", mediaY())
    print("La Covarianza es: ", covarianza())
    print("La Varianza en X es: ", varianzaX())
    print("La Varianza en Y es: ", varianzaY())
    print("El valor de Pearson es: ", pearson())