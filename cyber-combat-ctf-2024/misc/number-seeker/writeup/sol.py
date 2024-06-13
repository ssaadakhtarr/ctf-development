from pwn import *

def binary_search_guess(io, min_val, max_val):
    attempts = 0
    found = False
    while min_val <= max_val:
        if (not found):
           
            guess = (min_val + max_val) // 2
            
            io.sendline(str(guess))
            response = io.recvline().decode().strip()

            if "correct" in response:
                found = True
                print(io.recvuntil(":"))
                return guess, attempts
            elif "Too high" in response:
                max_val = guess - 1
            elif "Too low" in response:
                min_val = guess + 1

            attempts += 1

        else:
            break
        

    return None, attempts

def main():
    host = '64.227.172.20'
    port = 9000

    io = remote(host, port)
    total_attempts = 0

    for i in range(50):
        # Read initial instruction from the server
        initial_prompt = io.recvuntil(b"Enter your guess: ")

        min_val = 1
        max_val = 1000
        number, attempts = binary_search_guess(io, min_val, max_val)
        total_attempts += attempts

        if number is None:
            print(f"Failed to guess number {i + 1}")
            return
        print(f"Guessed number {i + 1}: {number} in {attempts} attempts")

    # Receive and print the flag
    flag = io.recvline().decode().strip()
    print(f"Flag: {flag}")

    io.close()

if __name__ == "__main__":
    main()
