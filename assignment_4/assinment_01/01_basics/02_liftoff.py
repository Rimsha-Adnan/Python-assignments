def main():
    # Start a countdown from 10 to 1
    for i in range(10, 0, -1):  # range(start, stop, step) with step -1 to countdown
        print(i, end=" ")  # Print each number followed by a space, without a newline
    print("Liftoff!")  # After the countdown, print "Liftoff!"

# This provided line is required at the end of the file to call the main() function.
if __name__ == '__main__':
    main()
