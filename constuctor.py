from os import system


def run():
    f = open('divisas_activas.txt', 'r')
    divisas = f.readlines()
    f.close()
    f = open('model.txt', 'r')
    model = f.readlines()
    f.close()
    for i in divisas:
        name = i.replace("\n", "")
        f = open(name + '.py', 'w')
        model[6] = f'divisa = "{str(name)}"\n'
        for k in model:
            k.replace("\n", "")
            if "divisa = ''" in k:
                k.replace("divisa = ''", "hola")
                print(k)
            f.write(str(k))
        f.close()
    f = open('instancias.bat', 'w')
    f.write('ECHO' + '\n')
    f.write('cd E:\JOSE_AMIGO\Desktop\DB"' + '\n')
    for i in divisas:
        name = i.replace("\n", "")
        f.write('start python ' + str(name) + '.py' + '\n')
    f.close()
    system("cd E:\JOSE_AMIGO\Desktop\DB")
    system("instancias.bat")


if __name__ == '__main__':
    run()
