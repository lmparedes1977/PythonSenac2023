class CPF:
    def __init__(self, cpf) -> None:
        valida_cpf = str(cpf)
        while not valida_cpf.isnumeric():
            valida_cpf.replace('.', '').replace('-', '')
        if len(valida_cpf) < 11:
            valida_cpf = (11-len(valida_cpf))*'0' + valida_cpf
        self.cpf = valida_cpf

    def valida_cpf(self):
        cpf_str = list(self.cpf)
        soma = 0
        mult = 10

        for i in range(9):
            soma += int(cpf_str[i]) * mult
            mult -= 1

        digito_1 = soma % 11 if (soma % 11) < 2 else 11 - (soma % 11)

        if digito_1 != int(cpf_str[9]):
            return f'\033[31mDIGITO VERIFICADOR INVÁLIDO\033[m'

        soma = 0
        mult = 11
        for i in range(10):
            soma += int(cpf_str[i]) * mult
            mult -= 1

        digito_2 = soma % 11 if (soma % 11) < 2 else 11 - (soma % 11)

        if digito_2 != int(cpf_str[10]):
            return f'\033[31mDIGITO VERIFICADOR INVÁLIDO\033[m'

        return f'\033[32mCPF VÁLIDO\033[m'


meu_cpf = CPF(1908424079)

print(meu_cpf.valida_cpf())
