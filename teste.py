from validate_docbr import CPF


validar_cpf = "012.345.678-90"
cpf = CPF()
cpf.validate(validar_cpf)
if validar_cpf:
    print('cpf valido')
else:
    print("cpf invalido")