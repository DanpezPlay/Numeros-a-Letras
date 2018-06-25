def numero_a_letras(numeros):
    MAX_NUMERO = 999999999
    unidades = ['CERO', 'UNO', 'DOS', 'TRES', 'CUATRO', 'CINCO', 'SEIS', 'SIETE', 'OCHO', 'NUEVE']
    decenasUnidad = ['DIEZ', 'ONCE', 'DOCE', 'TRECE', 'CATORCE', 'QUINCE', 'DIECISEIS', 'DIECISIETE', 'DIECIOCHO', 'DIECINUEVE']
    decenas = ['', 'DIEZ', 'VEINTE', 'TREINTA', 'CUARENTA', 'CINCUENTA', 'SESENTA', 'SETENTA', 'OCHENTA', 'NOVENTA']
    cientos = ['', 'CIENTO', 'DOSCIENTOS', 'TRESCIENTOS', 'CUATROCIENTOS', 'QUINIENTOS', 'SEISCIENTOS', 'SETECIENTOS', 'OCHOCIENTOS', 'NOVECIENTOS']

    cantidad = len(numeros)
    pesos = numeros[:cantidad-3]
    intPesos = int(pesos)
    centavos = numeros[cantidad-2:]

    def obtenerUnidad(numero):
        strPesos = unidades[numero]
        return strPesos

    def obtenerDecena(numero):
        if numero <= 19:
            strPesos = decenasUnidad[numero-10]
            return strPesos
        elif numero <= 29:
            if numero == 20:
                return decenas[2]
            else:
                strPesos = unidades[numero-20]
                return 'VEINTI' + strPesos
        elif numero <= 99:
            aux = numero/10
            strDecena = decenas[aux]
            strPesos = unidades[numero-(aux*10)]
            if strPesos == 'CERO':
                return strDecena
            else:
                return strDecena + ' Y ' + strPesos

    def obtenerCentena(numero):
        if numero == 100:
            return 'CIEN'
        else:
            aux = numero/100
            strCentena = cientos[aux]
            aux = numero-(aux*100)

            if aux == 0:
                return strCentena
            if aux <= 9:
                return strCentena + ' ' + obtenerUnidad(aux)
            elif aux <= 99:
                return strCentena + ' ' + obtenerDecena(aux)

    def obtenerMiles(numero):
        if numero == 1000:
            return 'MIL'
        else:
            miles = numero/1000
            aux = numero - ((numero/1000)*1000)
            if miles == 1:
                strMiles = 'MIL'
            elif miles <= 9:
                strMiles = obtenerUnidad(miles) + ' MIL'
            elif miles <= 99:
                strMiles = obtenerDecena(miles) + ' MIL'
            elif miles <= 999:
                strMiles = obtenerCentena(miles) + ' MIL'

            if aux == 0:
                return strMiles
            elif aux <= 9:
                return strMiles + ' ' + obtenerUnidad(aux)
            elif aux <= 99:
                return strMiles + ' ' + obtenerDecena(aux)
            elif aux <= 999:
                return strMiles + ' ' + obtenerCentena(aux)

    def obtenerMillones(numero):
        if numero == 1000000:
            return 'UN MILLON'
        else:
            millones = numero/1000000
            aux = numero - ((numero/1000000)*1000000)
            if millones == 1:
                strMillones = 'UN MILLON'
            elif millones <= 9:
                strMillones = obtenerUnidad(millones) + ' MILLONES'
            elif millones <= 99:
                strMillones = obtenerDecena(millones) + ' MILLONES'
            elif millones <= 999:
                strMillones = obtenerCentena(millones) + ' MILLONES'

            if aux == 0:
                return strMillones
            if aux <= 9:
                return strMillones + ' ' + obtenerUnidad(aux)
            elif aux <= 99:
                return strMillones + ' ' + obtenerDecena(aux)
            elif aux <= 999:
                return strMillones + ' ' + obtenerCentena(aux)
            elif aux <= 999999:
                return strMillones + ' ' + obtenerMiles(aux)

    if intPesos > MAX_NUMERO:
        return 'La cantidad sobrepasa lo admitido.'
    elif intPesos < 0:
        return 'Cantidades negativas no son admitidas.'
    elif intPesos <= 9:
        return obtenerUnidad(intPesos) + ' ' + centavos + '/100'
    elif intPesos <= 99:
        return obtenerDecena(intPesos) + ' ' + centavos + '/100'
    elif intPesos <= 999:
        return obtenerCentena(intPesos) + ' ' + centavos + '/100'
    elif intPesos <= 999999:
        return obtenerMiles(intPesos) + ' ' + centavos + '/100'
    elif intPesos <= 999999999:
        return obtenerMillones(intPesos) + ' ' + centavos + '/100'

        

numeros = input('Ingrese su numero: ')
numeros = str('{:.2f}'.format(float(numeros)))

numeroEnLetra = numero_a_letras(numeros)
print(numeroEnLetra)