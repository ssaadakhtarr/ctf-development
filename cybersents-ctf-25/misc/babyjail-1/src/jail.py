def jailed_input():
    banned = ['import', 'eval', 'exec', 'os', 'subprocess', 'sys', 'open']

    while True:
        user_input = input(">>> ")

        if user_input.strip().lower() == "exit":
            print("Goodbye!")
            break

        if any(bad in user_input for bad in banned):
            print("You're not allowed to use that.")
            continue

        try:
            result = eval(user_input)
            print(result)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    jailed_input()
