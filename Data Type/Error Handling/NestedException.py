try:
    f= open("test.txt",mode='r')
    my_file=f.read()
    print(my_file)
except Exception as e:
    print(f"\033[91m{e}\033[0m")
else:
    print("\033[92mFile read successfully!\033[0m")
finally:
    try:
        f.close()
    except Exception as e:
        #print(f"\033[91m{e}\033[0m")
        pass

print("\033[96mRest of the code execution continues...\033[0m")
