from linecache import getline

with open("database.txt", "r") as file:
    lines = len(file.readlines()) - 1

end = False
while end == False:
    with open("database.txt", "r") as file:
        command = input("Type anything (or type quit to quit): ")
        n = 1
        question = "question: %s" % command
        if command == "quit":
            break
        for line in file:
            if  question.lower()in line:
                if n % 2 != 0:
                    print(getline("database.txt" ,n+1))
                    break
            if n == lines:
                print("I don't have an answer...")
                choice = input("Add an answer for this question? (y/n): ")
                if choice in ("y", "n"):
                    if choice == "y":
                        answer = input(f"Answer for '{question}': ")
                        with open("database.txt", "a") as write:
                            write.writelines("%s\n" % question.lower())
                            write.writelines("%s\n" % answer.lower())
                            print("Added to database, restart the bot to see the answer working...")
                            break
                    else:
                        print("Ok...")
                        break
                else:
                    print("Invalid input")
                    break
            else:
                n += 1