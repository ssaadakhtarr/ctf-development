def jailed_input():
    banned = [
        "import", "eval", "exec", "open", "os", "sys", "subprocess", "input",
        "globals", "locals", "getattr", "setattr", "delattr", "compile",
        "__", "builtins", "class", "base", "subclasses"
    ]

    while True:
        try:
            user_input = input(">>> ")
            if user_input.strip().lower() == "exit":
                print("Goodbye!")
                break

            if any(b in user_input.lower() for b in banned):
                print("Access Denied.")
                continue

            result = eval(user_input, {"__builtins__": {}})
            print(result)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    jailed_input()
