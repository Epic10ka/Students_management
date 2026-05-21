from time import sleep
import json

def save_data(data):
    with open('group.json', 'w') as file:
        json.dump(data, file, indent=4)

def load_data():
    try:
        with open('group.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []


group = load_data()

def erro_num(msg):
    print()

    print('\033[1;97m┌────────────────────────────────────┐'.center(50))
    print(f'   [\033[1;91mERROR\033[1;97m] {msg}    '.center(55))
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
        # MENUS
        'access_menu': 'ACESSAR MENU         |',
        'main_menu': 'REGISTRO DE ALUNOS       /',      #TÍTULO DO MENU
        'back': '\033[1;97mRETORNANDO AO MENU',    #MENSSAGEM DE RETORNO
        'add': '\033[1;97mADICIONAR ALUNOS   /',      #TÍTULO DE ADICIONAR ALUNO
            'sub_add': '    \033[1;97mADICIONAR ALUNO           |',  #SUB TÍTULO DE ADICIONAR ALUNO
            'grade': 'Nota: ',
        'edit': '\033[1;97mEDITAR ALUNOS    /',     #TÍTULO DE EDITAR ALUNO
            'sub_edit': '\033[1;97mEDITAR ALUNO            |',
            'edit_again': 'Deseja editar novamente?: ', #Editar novamente
            'success_edit': '| ESTUDANTE editado com \033[1;92mSUCESSO \033[1;97m|',
        'remove_student': '\033[1;91mREMOVER\033[1;97m ALUNO        |'.center(35),    #TÍTULO DE REMOVER ALUNO
            'select_student': ' | SELECIONE UM ESTUDANTE | ', #SELECIONAR ALUNO
            'selected': '\033[1;94mALUNO SELECIONADO\033[1;97m:', #SELECTED
        'list': 'LISTAR ALUNOS  /',        #TITULO DE LISTAR ALUNOS
            'pupil': 'ALUNO',
            'grades': 'NOTAS',
        'exit': '\033[1;91mSAIR\033[1;97m     /',      #TÍTULO DE SAIR
            'sub_exit': '\033[1;91mSAIR\033[1;97m                 |', #SUB EXIT
        'name': 'Nome', #Nome
        'success_remove': '| ESTUDANTE removido com \033[1;92mSUCESSO \033[1;97m|'.center(55),  #MENSSAGEM DE SUCESSO (REMOVER)
            'remove_again': 'Deseja remover outro aluno?: ', #PERGUNTA (REMOVER)
        'success_add': '| ESTUDANTE registrado com \033[1;92mSUCESSO \033[1;97m|'.center(55),   #MENSSAGEM DE SUCESSO (ADICIONAR)
            'add_again': '   Deseja registrar outro estudante?: ', #Pergunta (ADICIONAR)
        'no_student': 'NENHUM ALUNO REGISTRADO', #SEM REGISTRO DE ALUNO
        # Inválidos
        'type_valid': 'Digite um número válido', #Digite um válido
        'invalid_opt': 'OPÇÃO INVÁLIDA', #OPÇÃO INVÁLIDA
        'invalid_num': 'NÚMERO INVÁLIDO', #NÚMERO INVÁLIDO
        #SAIDA
        'exit_msg': 'Fechando software'.center(42)
    },

    'en': {
        'returning': '\033[1;97mRETURNING TO MAIN MENU'.center(48),
        # MENUS
        'access_menu': 'ACCESS MENU          |',
        'main_menu': r'STUDENTS REGISTRATION    /',      #MENU TITLE
        'back': '\033[1;97mRETURNING TO MENU',    # RETURN MESSAGE
        'add': '\033[1;97mADD STUDENTS       /',     #ADD STUDENTS TITLE
            'sub_add': '\033[1;97mADD STUDENT            |'.center(45),  #ADD STUDENTS SUB TITLE
            'grade': 'Grade: ',
        'edit': '\033[1;97mEDIT STUDENTS    /',     #EDIT STUDENTS TITLE
            'sub_edit': '\033[1;97mEDIT STUDENT            |',
            'edit_again': 'Want to edit again?: ', #Edit again
            'success_edit': '\033[1;97m| STUDENT \033[1;92mSUCCESSFULLY \033[1;97m EDITED|',
        'remove_student': '\033[1;91mREMOVE\033[1;97m STUDENT       |',    #REMOVE STUDENT TITLE
            'select_student': ' | SELECT A STUDENT | ', #SELECT STUDENT
            'selected': '\033[1;94mSTUDENT SELECTED\033[1;97m:', #SELECTED
        'list': 'LIST STUDENTS  /',        #LIST STUDENTS TITLE
            'pupil': 'STUDENT',
            'grades': 'GRADES',
        'exit': '\033[1;91mEXIT\033[1;97m     /',     #EXIT TITLE
            'sub_exit': '\033[1;91mEXIT\033[1;97m                 |', #SUB EXIT
        'name': 'Name', #Name
        'success_remove': '| STUDENT \033[1;92mSUCCESSFULLY\033[m \033[1;97mREMOVED |', #SUCCESS MESSAGE (REMOVE)
            'remove_again': 'Want to remove another student?: ', #QUESTION (REMOVE)
        'success_add': '| STUDENT \033[1;92mSUCCESSFULLY\033[m \033[1;97mADDED |',  #SUCCESS MESSAGE (ADD)
            'add_again': '   Want to add another student?: ', #Question (ADD)
        'no_student': 'NO REGISTERED STUDENT',          #NO STUDENT REGISTER
        # Invalids
        'type_valid': 'Type a valid number',   #Type a valid
        'invalid_opt': 'INVALID OPTION', #INVALID OPTION
        'invalid_num': 'INVALID NUMBER', #INVALID NUMBER
        #EXIT
        'exit_msg': 'Finishing software.'.center(42)
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
    print(f'\n{t['returning']}'+'\n')
    timer(0.8)


def add_student():
    while True:
        print()
        print('┌────────────────────────────────────┐')
        print(f'|      {t['sub_add']}               ')
        print('└────────────────────────────────────┘')
        print()

        name = (input(f'        {t['name']}: ')).title().strip()
        try:
            student = [name]
            for g in range(1, 4):
                grade = float(input(f'        {g}° {t['grade']}: '))
                student.append(grade)

            group.append(student.copy())
            save_data(group)

            student.clear()

            print()
            timer(0.2)
            print()
            print(f'{t['success_add']}'.center(55))
            print()

        except ValueError:
            erro_num(f'{t['invalid_num']}')
            continue

        again = input(f'   {t['add_again']} ').strip().upper()[0]

        if again == 'N':
            break
        else:
            continue


def remover():

    if not group:
        print()
        print(f'{t['no_student']}'.center(40))
        print()
        timer(0.5)
        return

    print()
    print('┌────────────────────────────────────┐')
    print(f'           {t['remove_student']}')
    print('└────────────────────────────────────┘')
    print()

    while True:

        for num, name in enumerate(group, start=1):
            print(f'[{num}] {name[0]}', end=' | ')
            print()
            print()
        print(f'{t['select_student']}'.center(40))

        try:
            remove = int(input('                 > '))-1  # -1 to go at the previous index (better to visualize 1 than 0)

            if 0 <= remove < len(group):
                group.pop(remove)
                save_data(group)
                print()
                print(f'{t['success_remove']}'.center(55))
                print()

                if group:
                    while True:
                        again = input(f'{t['remove_again']}').strip().upper()[0]
                        if again == 'N':
                            return
                        elif again in 'YS':
                            print()
                            timer(0.2)
                            break
                        else:
                            erro_num(f'{t['invalid_opt']}')
                elif not group:
                    print()
                    print(f'{t['no_student']}'.center(40))
                    print()
                    timer(0.5)
                    return

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
        print(f'|           [1] {t['access_menu']}')
        print(f'|           [2] {t['remove_student']}')
        print(f'|           [3] {t['sub_exit']}')
        print('└────────────────────────────────────┘')
        print()
        choice = input('                 > ')
        while True:

            if choice == '1':
                if not group:
                    print()
                    print(f'{t['no_student']}'.center(40))
                    print()
                    timer(0.5)
                    return
                print()
                print('┌────────────────────────────────────┐')
                print(f'|            {t['sub_edit']}')
                print('└────────────────────────────────────┘')
                print()
                for num, nome in enumerate(group):
                    print(f'[{num + 1}] {nome[0]}', end=' | ')
                sleep(0.5)
                print()
                print()

                while True:
                    try:
                        print(f'{t['select_student']}'.center(35))
                        print()
                        new_student = int(input('                 > '))
                        print()
                        print(f'    {t['selected']} {group[new_student-1] [0]}')
                        print()
                        name = (input(f'        {t['name']}: ')).title().strip()
                        group[new_student - 1][0] = name
                        for g in range(1, 4):
                            grade = input(f'        {g}° {t['grade']}')
                            group[new_student-1][g] = grade
                        print()
                        print(f'{t['success_edit']}'.center(55))
                        print()

                        while True:
                            again = input(f'{t['edit_again']}').strip().upper()[0]
                            if not group:
                                break
                            if again == 'N':
                                return
                            elif again in 'YS':
                                print()
                                break
                        if again == 'S':
                            break
                    except ValueError:
                        print()
                        erro_num(f'{t['invalid_num']}')
                        continue


            elif choice == '2':
                remover()
                break

            elif choice == '3':
                print()
                timer(0.4)
                return

            else:
                print()
                erro_num(f'{t['invalid_opt']}')
                sleep(1)


def list_student():
    if not group:
        returning(f'{t['no_student']}')
        return

    for a in group:
        print(f'\n\033[1;94m{t['pupil']}: \033[1;97m{a[0]} | \033[1;92m{t['grades']}\033[1;97m: [{a[1]}], [{a[2]}], [{a[3]}] ' + '\n')
        print()
    sleep(1)


def exit_msg(msg):
    print(f'\n{msg}\n')
    sleep(0.6)
    timer(0.6)
    exit()

def menu():

    options = {
        '1': add_student,
        '2': edit_student,
        '3': list_student,
        '4': lambda: exit_msg(f'{t['exit_msg']}')
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