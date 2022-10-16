def num_check(question):
    error = "Please enter a whole digit number"

    valid = False
    while not valid:
        try:
            response = int(input(question))
            return response

        except ValueError:
            print(error)


question = num_check("2+4=")
