from time import sleep

student = []
group = []

def erro_num(msg):
    print()

    print('\033[1;97m┌────────────────────────────────────┐'.center(50))
    print(f'   [\033[1;91mERROR\033[1;97m] {msg}.   '.center(55))
    print('└────────────────────────────────────┘'.center(42))
    print()


def timer(x):
    for c in range(0, 3):
        print('*'.center(40))
        sleep(x)


#LANGUAGE DICTIONARY
language = {
    'ptbr': {
        'returning': '\033[1;97mRETORNANDO AO MENU'.center(45),
        'main_menu': 'REGISTRO DE ALUNOS       /',      #TÍTULO DO MENU
        'back': '\033[1;97mRETORNANDO AO MENU',    #MENSSAGEM DE RETORNO
        'add': '\033[1;97mADICIONAR ALUNOS   /',      #TÍTULO DE ADICIONAR ALUNO
            'sub_add': '    \033[1;97mADICIONAR ALUNO           |',  #SUB TÍTULO DE ADICIONAR ALUNO
            'grade': 'Nota: ',
        'edit': '\033[1;97mEDITAR ALUNOS    /',     #TÍTULO DE EDITAR ALUNO
        'remove_student': '\033[1;91mREMOVER\033[1;97m ALUNO            |'.center(35),    #TÍTULO DE REMOVER ALUNO
            'select_student': ' | SELECIONE UM ESTUDANTE | ',
        'remove_again': 'Deseja remover outro aluno?: ', #PERGUNTA (REMOVER)
        'list': 'LISTAR ALUNOS  /',        #TITULO DE LISTAR ALUNOS
        'exit': '\033[1;91mSAIR\033[1;97m     /',      #TÍTULO DE SAIR
        'name': 'Nome', #nome
        'success_remove': '| ESTUDANTE removido com \033[1;92mSUCESSO\033[m \033[1;97m|'.center(55),  #MENSSAGEM DE SUCESSO (REMOVER)
        'success_add': '| ESTUDANTE registrado com \033[1;92mSUCESSO\033[m \033[1;97m|'.center(55),   #MENSSAGEM DE SUCESSO (ADICIONAR)
        'add_again': '   Deseja registrar outro estudante?: ', #PERGUNTA (ADICIONAR)
        'no_student': 'NENHUM ALUNO REGISTRADO', #SEM REGISTRO DE ALUNO
        #invalidos
        'invalid_num': 'Digite um número válido', #Numero válido
        'invalid_opt': 'OPÇÃO INVÁLIDA' #Opção válida

    },

    'en': {
        'returning': '\033[1;97mRETURNING TO MAIN MENU'.center(48),
        'main_menu': r'STUDENTS REGISTRATION    /',      #MENU TITLE
        'back': '\033[1;97mRETURNING TO MENU',    # RETURN MESSAGE
        'add': '\033[1;97mADD STUDENTS       /',     #ADD STUDENTS TITLE
            'sub_add': '\033[1;97mADD STUDENT',  #ADD STUDENTS SUB TITLE
            'grade': 'Grade: ',
        'edit': '\033[1;97mEDIT STUDENTS    /',     #EDIT STUDENTS TITLE
        'remove_student': '\033[1;91mREMOVE\033[1;97m STUDENT  ',    #REMOVE STUDENT TITLE
            'select_student': ' | SELECT A STUDENT | ',
        'remove_again': 'Want to remove another student?: ', #QUESTION (REMOVE)
        'list': 'LIST STUDENTS  /',        #LIST STUDENTS TITLE
        'exit': '\033[1;91mEXIT\033[1;97m     /',     #EXIT TITLE
        'name': 'Name', #name
        'success_remove': '| STUDENT \033[1;92mSUCCESSFULLY\033[m \033[1;97mREMOVED |', #SUCCESS MESSAGE (REMOVE)
        'success_add': '| STUDENT \033[1;92mSUCCESSFULLY\033[m \033[1;97mADDED |',  #SUCCESS MESSAGE (ADD)
        'add_again': '   Want to add another student?: ', #QUESTION (ADD)
        'no_student': 'NO REGISTERED STUDENT',          #NO STUDENT REGISTER
        #invalids
        'invalid_num': 'Type a valid number',   #valid number
        'invalid_opt': 'INVALID OPTION', #Valid option
    }
}
#LANGUAGE DICTIONARY


while True:

    print()
    lang = input('\033[1;97mSelect a language / Escolha um idioma [\033[1;34men\033[1;97m/\033[1;92mpt\033[1;93mbr\033[1;97m]: ').strip().lower().replace(' ', '')
    if lang not in ('ptbr', 'en'):
        erro_num('INVALID LANGUAGE')
        lang = 'en'
        t = language.get(lang, language['en'])

    else:
        t = language.get(lang, language['en'])  # define en as default langauge | made it out of the 'while' loop so the variable 't' is visible.
        break

def returning(msg):
    sleep(0.2)
    erro_num(msg)
    print()
    print(f'{t['returning']}')
    print()
    timer(0.8)


def add_student():
    while True:
        print()
        print('┌────────────────────────────────────┐')
        print(f'|      {t['sub_add']}               ')
        print('└────────────────────────────────────┘')
        print()

        name = (input(f'        {t['name']}: ')).title().strip()
        student.append(name)
        try:
            for g in range(1, 4):
                grade = float(input(f'        {g}° {t['grade']}: '))
                student.append(grade)

            group.append(student[:])
            student.clear()

            print()
            timer(0.2)
            print()
            print(f'{t['success_add']}'.center(55))
            print()

        except ValueError:
            erro_num(f'{t['valid_num']}')
            continue

        again = input(f'   {t['add_again']} ').strip().upper()[0]

        if again == 'N':
            break
        else:
            continue


def remover():
    print()
    print('┌────────────────────────────────────┐')
    print(f'|           {t['remove_student']}')
    print('└────────────────────────────────────┘')
    print()
    while True:
        for num, name in enumerate(group, start=1):
            print(f'[{num}] {name[0]}', end=' | ')
        print()
        print()
        print(f'{t['select_student']}'.center(40))
        print()

        try:
            remove = int(input('                 > '))-1  # -1 to go at the previous index (better to visualize 1 than 0)

            if 0 <= remove < len(group):
                group.pop(remove)
                print()
                print(f'{t['success_remove']}'.center(55))
                print()
                while True:
                    again = input(f'{t['remove_again']}').strip().upper()[0]
                    if not group:
                        erro_num(f'{t['no_student']}')
                        timer(0.5)
                        return
                    if again == 'N':
                        return
                    elif again in 'YS':
                        print()
                        timer(0.8)
                        break
                    else:
                        erro_num(f'{t['invalid_opt']}')

            else:
                erro_num(f'{t['select_student']}')
                sleep(0.5)
                continue
        except (ValueError, IndexError):
            erro_num(f't{'invalid_opt'}')


def edit_student():
    if not group:
        returning(f'{t['no_student']}')
        return
    while True:
        print()
        print('\033[1;97m              MENU EDITAR')
        print('┌────────────────────────────────────┐')
        print('|           [1] ACESSAR MENU         |')
        print('|           [2] REMOVER ALUNO        |')
        print('|           [3] SAIR                 |')
        print('└────────────────────────────────────┘')
        print()
        choice = input('                 > ')
        while True:

            if choice == '1':
                print()
                print('┌────────────────────────────────────┐')
                print('|            \033[1;97mEDITAR ALUNO            |')
                print('└────────────────────────────────────┘')
                print()
                for num, nome in enumerate(group):
                    print(f'[{num + 1}] {nome[0]}', end=' | ')
                sleep(0.5)
                print()
                print()

                while True:
                    try:
                        print(' | SELECIONE O ALUNO | '.center(40))
                        print()
                        new_student = int(input('                 > '))
                        print()
                        print(f'        \033[1;94mstudent SELECIONADO\033[m\033[1;97m: {group[new_student-1] [0]}')
                        print()
                        name = (input('        Nome do estudante: ')).title().strip()
                        g1 = float(input('        1ª nota: '))
                        g2 = float(input('        2ª nota: '))
                        g3 = float(input('        3ª nota: '))
                        group[new_student-1][0] = name
                        group[new_student-1][1] = g1
                        group[new_student-1][2] = g2
                        group[new_student-1][3] = g3
                        print()
                        print('| ESTUDANTE editado com \033[1;92mSUCESSO\033[m \033[1;97m|'.center(55))
                        print()

                        while True:
                            again = input('Deseja editar novamente?: ').strip().upper()[0]
                            if again == 'N':
                                return
                            elif again == 'S' or again == 'Y':
                                print()
                                break
                        if again == 'S':
                            break
                    except ValueError:
                        print()
                        erro_num('NÚMERO INVÁLIDO.')
                        continue


            elif choice == '2':
                remover()

            elif choice == '3':
                print()
                timer(0.8)
            else:
                print()
                erro_num(f'{t['invalid_opt']}')
                sleep(1)


def list_student():
    if not group:
        returning(f'{t['no_student']}')
        return
    print()
    for a in group:
        print(f'\033[1;94mALUNO: \033[1;97m{a[0]} | \033[1;92mNOTAS\033[1;97m: [{a[1]}], [{a[2]}], [{a[3]}] ')
        print()
    sleep(1)



def menu():

    options = {
        '1': add_student,
        '2': edit_student,
        '3': list_student
    }

    while True:

        print()
        print('\033[1;97m   \──────────────────────────────────/')
        print(rf'    \       {t['main_menu']}       ')
        print('     \──────────────────────────────/')
        print(rf'      \     [1] {t['add']}   ')
        print(rf'       \                          /')
        print(rf'        \   [2] {t['edit']}    ')
        print(rf'         \                      /')
        print(rf'          \ [3] {t['list']}')
        print(rf'           \                  /')
        print(rf'            \  [4]  {t['exit']}     ')
        print()

        opt = input('                    > ')
        choice = options.get(opt)

        if  choice:
            choice()
        else:
            erro_num('Opção INVÁLIDA')
menu()