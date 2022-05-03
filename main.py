import os
import pandas as pd
from iqoptionapi.stable_api import IQ_Option
from os import system


def run():
    aux = []
    while True:
        Iq = IQ_Option("cognito802@gmail.com", "0lg4ch4v3z")
        Iq.connect()
        all_assets = pd.DataFrame(Iq.get_all_open_time())
        divisasTB = all_assets.loc[:, ['binary', 'turbo']]
        divisasTB = divisasTB.dropna()
        divisasActivas = divisasTB.loc[:, ['turbo']] == [{'open': True}]
        div = divisasActivas.to_dict('dict')
        div = list(div.values())
        div = dict(div[0])
        div = sorted(div.items())
        div = dict(div)
        if div != aux:
            os.system('taskkill /F /IM cmd.exe')
            aux = div
            with open('divisas_activas.txt', 'w') as f:
                for key, value in div.items():
                    if value:
                        f.write(str(key) + '\n')
            f.close()
            system("cd E:\JOSE_AMIGO\Desktop\DB")
            system("constuctor.py")


if __name__ == '__main__':
    run()
