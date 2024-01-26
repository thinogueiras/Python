from faker import Faker

faker = Faker()

nome = faker.name()
primeiro_nome_fem = faker.first_name_female()
usuario = faker.user_name()
senha = faker.password()
mes = faker.month()

print(f'Nome: {nome}')
print(f'Nome feminino: {primeiro_nome_fem}')
print(f'Usuário: {usuario}')
print(f'Senha: {senha}')
print(f'Mês: {mes}')
