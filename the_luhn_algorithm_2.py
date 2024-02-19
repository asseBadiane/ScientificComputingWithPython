"""
L'algorithme de Luhn est une méthode utilisée pour vérifier la validité d'un numéro d'identification tel qu'un numéro 
de carte de crédit ou un numéro de sécurité sociale. Voici une explication détaillée de l'algorithme :
À partir de la droite vers la gauche, doubler la valeur de chaque deuxième chiffre :

Commencez par le chiffre le plus à droite et doublez chaque deuxième chiffre en déplaçant vers la gauche. 
Si le double d'un chiffre est supérieur à 9, soustrayez 9 de ce double.
Additionner tous les chiffres :
Ajoutez tous les chiffres obtenus après avoir doublé les chiffres et soustrait 9 si nécessaire.
Vérifier si la somme des chiffres est un multiple de 10 :
Si la somme de tous les chiffres est un multiple de 10, alors le numéro est valide selon l'algorithme de Luhn. 
Sinon, le numéro n'est pas valide.
"""


def verify_card_number(card_number):
    sum_of_odd_digits = 0  # sum of odd digits
    card_number_reversed = card_number[::-1]  # reverse the card number
    odd_digits = card_number_reversed[::2]  # get the odd digits

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0  # sum of even digits
    even_digits = card_number_reversed[1::2]  # get the even digits
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    print(total)
    return total % 10 == 0


def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')


main()
