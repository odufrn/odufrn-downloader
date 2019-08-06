files_test = [
    'test_env', 'test_dataset', 'test_group',
]

for filename in files_test:
    exec(open("./{}.py".format(filename)).read())
    print("{} executado com sucesso!".format(filename))
