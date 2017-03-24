user_names = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
              'swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
              'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

name = input("Enter user name: ")

if name in user_names:
    print("Access Granted")
else:
    print("Access Denied")
