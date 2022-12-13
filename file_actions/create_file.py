import os
import pandas as pd

class CreateFile:
    def __init__(self, dados, name_file, heads):
        self.dados = dados
        self.name_file = name_file
        self.heads = heads
        self.create_file_csv()
        pass

    def create_file_csv(self):
        # Cria a pasta "./raw_files/fat/" caso ela não exista
        os.makedirs('./raw_files/fat/', exist_ok=True)

        # Cria a pasta "./raw_files/dm/" caso ela não exista
        os.makedirs('./raw_files/dm/', exist_ok=True)

        try:
            df = pd.DataFrame(self.dados).reset_index().dropna(axis=0, how='all')
            df = df.apply(lambda x: x.astype(str).str.upper())
            df.columns = self.heads
            if len(df.columns) > 3:
                df.to_csv(f"./raw_files/fat/{self.name_file}.csv", sep=",", index=False)
            else:
                df.to_csv(f"./raw_files/dm/{self.name_file}.csv", sep=",", index=False)
        except KeyError as error:
            print(f"Error in moment create file, non-existent value: {error}")
