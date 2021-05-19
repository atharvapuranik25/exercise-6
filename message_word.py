  def message_word(str):
    list = str.split(' ')
    list2 = list[0:30]
    str1 = " "
    print(str1.join(list2))
    # function to print the first 30 words of any string

message = input("Enter your message: ")
message_word(message)
