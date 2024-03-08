import time
def user_para():
    print("..........Welcome to the Typing Speed Test..........")
    user_input = input("Enter your Paragraph here : ")  # user entered para
    input("Press Enter when you are ready to start....")
    start_time = time.time()   # time started
    text_to_type = user_input
    print("Type the following text..")
    print(text_to_type)   # user defined para
    user_input = input("Enter : ")
    end_time = time.time()   # end time
    total_words = len(user_input.split())    # total words user typed
    time_taken = end_time - start_time          # calculate time taken
    typing_speed = (total_words / time_taken) * 60        # speed of words per seconds (/ 60 for find 1 min )
    if (list(user_input) == list(text_to_type)):     # check the words is given words
        print("You typed ", total_words, " words in ", "{:.2f}".format(time_taken), " seconds.")
        print("Your typing speed is ", "{:.2f}".format(typing_speed), " words per minute.")
    else:
        print("Entered words are wrong...............")


def write_para():
    print("..........Welcome to the Typing Speed Test..........")
    input("Press Enter when you are ready to start....")
    start_time = time.time()    # time started
    text_to_type = "A paragraph could contain a series of brief examples or a single long illustration of a general point"
    print("Type the following text..")
    print(text_to_type)
    user_input = input("Enter : ")
    end_time = time.time()      #  # time end
    total_words = len(user_input.split())
    time_taken = end_time - start_time
    typing_speed = (total_words / time_taken) * 60
    if (list(user_input) ==  list(text_to_type)):   # check the words is given words
        print("You typed ",total_words," words in ","{:.2f}".format(time_taken)," seconds.")
        print("Your typing speed is ","{:.2f}".format(typing_speed)," words per minute.")
    else:
        print("Entered words are wrong...............")


print("1). User defined Paragraph")   # choice ( 1 )
print("2). Pre defined Paragraph")    # choice ( 2 )
defined_para = int(input("Enter your choice : "))    # user choice ( 1 or 2 )

if (defined_para == 2 ):
    write_para()
else:
    user_para()





