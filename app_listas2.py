list_id = []
list_name = []
list_contact = []
list_e_mail = []
import os
def fnt_limpiar():
    os.system('cls')
    print('autor: aleXxxBb')
    print('fecha: 18 abril del 2024\n\n')
    
def fnt_registrar(id, name, contact, e_mail):
    if id == '' or contact == '' or e_mail == '' or name == '':
        enter = input('\nError, debe de ingresar todos los datos <ENTER>')
    else:
        list_id.append(id)
        list_name.append(name)
        list_contact.append(contact)
        list_e_mail.append(e_mail)
        enter = input('\nPersona registrada con exito <ENTER>')

def fnt_selector(opcion):
    fnt_limpiar()
    if opcion == '1':
        id = input('ID :  ')
        if id in list_id:
            enter = input('\nEsta persona ya se encuentra registrada <ENTER>')
        else: 
            name = input('Nombre :  ')
            contact = input('Contacto:  ')
            e_mail = input('Email:  ')
            fnt_registrar(id, name, contact, e_mail)
    elif opcion == '2':
        fnt_limpiar()
        for i in range(len(list_id)):
            print(f'{list_id[i]}, "   ",   {list_name[i]}, "   ",  {list_contact[i]}, "   ",  {list_e_mail[i]}')
        enter = input('\n<ENTER>')
            

sw = True 
while sw == True: 
    fnt_limpiar()
    op = input('\n\n<<<<< MENU PRINCIPAL >>>>>\n1. REGISTRAR\n2. CONSULTAR\n3. SALIR')
    fnt_selector(op)