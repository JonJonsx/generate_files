from file_actions.create_dm import SepareteColumns
from file_actions.create_fat import CreateFat

# criar as dimensoes com script
# fazer as fatos usando query

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    SepareteColumns().call_create_dimension()
    CreateFat().call_create_fat()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
