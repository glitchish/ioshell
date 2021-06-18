true=True
false=False
print("\033c",end='')
print("\033[31m⬤\033[32m⬤\033[36m⬤    \033[0;2mio shell <version:0.0.5|created:2021-6-18|creator:theiocoder>\033[0m")
while (true):
    shell = input("\033[1;2miosh ➜\033[0m ")
    stdin = shell.split(' ')
    help_list = [
        "print-ln/print-line <str>               prints <str> to the terminal\n",
        "exit <int>                              exits the repl with code <int>\n",
        "clear-terminal/clear-screen/clear-all   resets the terminal\n"
    ]
    if (stdin[0] == "exit"):
        if (shell != "exit"):
            exit("iosh exit with code "+stdin[1])
        else:
            exit("iosh exit")
    elif (stdin[0] == "print-line" or stdin[0] == "print-ln"):
        def setstr(s):
                if (" ".join(s)[0] == '"' and " ".join(s)[-1] == '"'):
                    return (" ".join(s).strip('"'))
                elif (" ".join(s)[0] == "'" and " ".join(s)[-1] == "'"):
                    return (" ".join(s).strip("'"))
                elif (" ".join(s)[0] == "'" and " ".join(s)[-1] == '"'):
                    print("error: you mismatched start and end quotes: "+" ".join(s))
                elif (" ".join(s)[0] == '"' and " ".join(s)[-1] == "'"):
                    print("error: you mismatched start and end quotes: "+" ".join(s))
                else:
                    print("error: print-line/ln doesn't support variables right now: "+stdin[1])
        print(setstr(stdin[1:]))
    elif (stdin[0] == "clear-terminal" or stdin[0] == "clear-screen" or stdin[0] == "clear-all"):
        print("\033c",end='')
        print("\033[31m⬤\033[32m⬤\033[36m⬤    \033[0;2mio shell <version:0.0.5|created:2021-6-18|creator:theiocoder>\033[0m")
    elif (stdin[0] == "help" or stdin[0] == "help-me"):
        print("currently supported commands/syntax:\n\n "+" ".join(help_list))
    else: print(stdin+" is an unknown command or syntax error, maybe try something else")
