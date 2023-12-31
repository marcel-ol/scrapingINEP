class banco:
    def __init__(self):
        import psycopg2 as pg
        self.conexao = pg.connect(
            host='127.0.0.1', database='postgres', user='postgres', password='1234')
        self.cursor = self.conexao.cursor()

    def instalaBanco(self):
        # CRIAR TABELA banco
        try:
            criarTabela = 'CREATE TABLE banco (id SERIAL PRIMARY KEY, login VARCHAR (20) NOT NULL, senha varchar (20) NOT NULL)'
            self.cursor.execute(criarTabela)
            self.conexao.commit()
            print("Tabela banco inserida.")
            # cria um novo banco padrao
            novolog = "INSERT INTO banco (login,senha) VALUES ('admin','1234')"
            self.cursor.execute(novolog)
            self.conexao.commit()
            print("Usuário admin senha 1234 criado.")
        except Exception as e:
            print("Tabela banco já criada. Exceção: %s" % (e))
            self.conexao.rollback()

        # CRIAR TABELA ALUNO
        try:
            criarTabela = 'CREATE TABLE aluno (matricula INT PRIMARY KEY , nome varchar (100) , av1 NUMERIC(4,2) , av2 NUMERIC(4,2) , av3 NUMERIC(4,2) , av4 NUMERIC(4,2))'
            self.cursor.execute(criarTabela)
            self.conexao.commit()
            print("Tabela ALUNO inserida.")
        except Exception as e:
            print("Tabela ALUNO já criada. Exceção: %s" % (e))
            self.conexao.rollback()

        # CRIAR TABELA LOG
        try:
            criarTabela = 'CREATE TABLE log (id SERIAL PRIMARY KEY , matricula INT NOT NULL , login VARCHAR (20) NOT NULL, dataHora TIMESTAMP NOT NULL DEFAULT NOW(), motivo varchar (144) )'
            self.cursor.execute(criarTabela)
            self.conexao.commit()
            print("Tabela LOG inserida.")
        except Exception as e:
            print("Tabela LOG já criada. Exceção: %s" % (e))
            self.conexao.rollback()

    def incluirbanco(self, login, senha):
        try:
            cadastrarbanco = 'INSERT INTO banco (login,senha) VALUES (%s,%s)'
            self.cursor.execute(cadastrarbanco, (login, senha))
            self.conexao.commit()
            return -1
        except Exception as e:
            print("Erro. Exceção: %s" % (e))
            self.conexao.rollback()
            return 0

    def loginbanco(self, login, senha):
        try:
            buscarbanco = 'SELECT id from banco where login = %s and senha = %s LIMIT 1'
            self.cursor.execute(buscarbanco, (login, senha))
            resultado = self.cursor.fetchone()
            if (resultado == None):
                raise Exception("Usuário/senha não conferem")
            else:
                print("Login realizado. Bem vindo(a), ", login)
                return resultado[0]
        except Exception as e:
            e = "Exceção: ," + str(e)
            return 0
