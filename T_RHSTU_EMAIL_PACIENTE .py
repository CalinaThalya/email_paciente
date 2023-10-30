##LINK para o GitHub:  https://github.com/CalinaThalya/email_paciente.git

# Eu importo as bibliotecas necessárias
from datetime import date
import random
import oracledb

# Eu estabeleço uma conexão com o banco de dados Oracle
db = oracledb.connect(user='rm552539', password='130701', dsn='oracle.fiap.com.br/orcl')
cursor = db.cursor()

# Eu faço uma consulta para obter IDs válidos da tabela T_RHSTU_PACIENTE
cursor.execute("SELECT ID_PACIENTE FROM T_RHSTU_PACIENTE")
valid_ids = [row[0] for row in cursor.fetchall()]

# Eu defino funções para gerar dados de e-mail aleatórios
def generate_email():
    domains = ["hotmail.com", "gmail.com", "yahoo.com", "icloud.com", "uol.com"]
    return f"{random.choice(domains)}"

# Eu defino funções para gerar dados de tipo de e-mail e status de e-mail aleatórios
def generate_tipo_email():
    tipos = ["pessoal", "trabalho", "outro"]
    return random.choice(tipos)

def generate_status_email():
    statuses = ["A", "I"]
    return random.choice(statuses)

# Eu crio um loop para inserir dados de e-mail
for i in range(1, 10000001):
    ID_PACIENTE = random.choice(valid_ids)  # Seleciono aleatoriamente um ID válido
    NM_USUARIO = 'USER'
    DS_EMAIL = generate_email()
    TP_EMAIL = generate_tipo_email()
    ST_EMAIL = generate_status_email()
    DT_CADASTRO = date.today()  # Data de cadastro

    # Eu defino a consulta de inserção
    insert_query = '''
        INSERT INTO T_RHSTU_EMAIL_PACIENTE (ID_PACIENTE, NM_USUARIO, DS_EMAIL, TP_EMAIL, ST_EMAIL, DT_CADASTRO)
        VALUES (:1, :2, :3, :4, :5, :6)
    '''

    # Eu defino os valores para a consulta
    values = (ID_PACIENTE, NM_USUARIO, DS_EMAIL, TP_EMAIL, ST_EMAIL, DT_CADASTRO)

    # Eu executo a consulta de inserção
    cursor.execute(insert_query, values)

    # Eu faço um commit para inserir os dados no banco de dados
    db.commit()

# Eu fecho o cursor e a conexão com o banco de dados
cursor.close()
db.close()

# Eu imprimo uma mensagem para indicar a conclusão da inserção de dados de e-mail
print("Inserção de dados de e-mail concluída.")
