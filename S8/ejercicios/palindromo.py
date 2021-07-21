def es_palindromo(texto):

    # Convierte cualquier string en minúsculas y elimina todos los caracteres no alfabéticos
    def toChar(texto):
        texto = texto.lower()
        ans = ''
        for letras in texto:
            if letras in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + letras
        return ans

    def esPal(texto):
        if len(texto) <= 1:
            return True
        else:
            return texto[0] == texto[-1] and esPal(texto[1:-1])

    return esPal(toChar(texto))

# Examples of calling isPalindrome()
print ("")
print ('Is eve a Palindrome?')
print (es_palindromo('eve'))

print ("")
print ('Is able was I ere saw Elba a Palindrome?')
print (es_palindromo('Able was I, ere I saw Elba'))