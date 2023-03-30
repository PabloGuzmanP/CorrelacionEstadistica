def matriz_correlacion(altura, peso, edad):
    def media(arreglo):
        return sum(arreglo) / len(arreglo)

    def covarianza(arreglo1, arreglo2, media1=None, media2=None):

        if len(arreglo1) != len(arreglo2):
            raise ValueError("Las listas deben tener la misma longitud.")
        if not arreglo1 or not arreglo2:
            return 0
        if not media1:
            media1 = media(arreglo1)
        if not media2:
            media2 = media(arreglo2)
        cov = sum((arreglo1[i] - media1) * (arreglo2[i] - media2) for i in range(len(arreglo1))) / len(arreglo1)
        return cov

    def coeficiente_correlacion(covarianza, desviacion1, desviacion2):
        return covarianza / (desviacion1 * desviacion2)

    # Calcular medias
    media_altura = media(altura)
    media_peso = media(peso)
    media_edad = media(edad)

    # Calcular desviaciones estandar
    desviacion_altura = (sum((x - media_altura) ** 2 for x in altura) / len(altura)) ** 0.5
    desviacion_peso = (sum((x - media_peso) ** 2 for x in peso) / len(peso)) ** 0.5
    desviacion_edad = (sum((x - media_edad) ** 2 for x in edad) / len(edad)) ** 0.5

    # Calcular matriz de covarianza
    matriz_covarianza = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    matriz_covarianza[0][0] = covarianza(altura, altura, media_altura, media_altura)
    matriz_covarianza[0][1] = matriz_covarianza[1][0] = covarianza(altura, peso, media_altura, media_peso)
    matriz_covarianza[0][2] = matriz_covarianza[2][0] = covarianza(altura, edad, media_altura, media_edad)
    matriz_covarianza[1][1] = covarianza(peso, peso, media_peso, media_peso)
    matriz_covarianza[1][2] = matriz_covarianza[2][1] = covarianza(peso, edad, media_peso, media_edad)
    matriz_covarianza[2][2] = covarianza(edad, edad, media_edad, media_edad)

    # Calcular matriz de correlacion
    matriz_corr = [[0] * 3 for i in range(3)]
    matriz_corr[0][0] = 1
    matriz_corr[0][1] = matriz_corr[1][0] = coeficiente_correlacion(matriz_covarianza[0][1], desviacion_altura,desviacion_peso)
    matriz_corr[0][2] = matriz_corr[2][0] = coeficiente_correlacion(matriz_covarianza[0][2], desviacion_altura,desviacion_edad)
    matriz_corr[1][1] = 1
    matriz_corr[1][2] = matriz_corr[2][1] = coeficiente_correlacion(matriz_covarianza[1][2], desviacion_peso,desviacion_edad)
    matriz_corr[2][2] = 1
    return matriz_corr

if __name__ == '__main__':
    altura = [1.70, 1.63, 1.75, 1.80, 1.68]
    peso = [65, 54, 75, 82, 63]
    edad = [28, 21, 35, 42, 27]
    corr_matrix =matriz_correlacion(altura, peso, edad)
    for fila in corr_matrix:
        print(fila)
