
def select_bd():  # Criado a funcao para selecionar o tipo do bd, entre postgre, oracle, etc
    db_program = str(
        input('Database: \n1 - Oracle \n2 - Postgre\nSelection: '))
    lists_dbs_ = {"1": "ORACLE","2": "POSTGRE"}
    count = 0
    while db_program not in lists_dbs_.keys():
        count += 1
        print('\nInvalid database value\n')
        db_program = str(
            input('Database: \n1 - Oracle \n2 - Postgre\nSelection: '))
        if count == 3:
            quit()
    print(type(db_program))
    return db_program
    


select_bd()
