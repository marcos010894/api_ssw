import random

def calculate_nfe_key_dv(nfe_key_without_dv):
    total = 0
    weights = [2, 3, 4, 5, 6, 7, 8, 9] * 6

    for index, digit in enumerate(reversed(nfe_key_without_dv)):
        total += int(digit) * weights[index]

    remainder = total % 11
    dv = 11 - remainder

    if dv > 9:
        dv = 0

    return dv

# Gerar 43 dígitos aleatórios
nfe_key_without_dv = "".join([str(random.randint(0, 9)) for _ in range(43)])

# Calcular o dígito verificador
dv = calculate_nfe_key_dv(nfe_key_without_dv)

# Combinar os 43 dígitos e o dígito verificador
fake_nfe_key = nfe_key_without_dv + str(dv)

print(fake_nfe_key)