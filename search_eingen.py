lines = (''' python is very good programing language . it is very popular in all over the world .
 it is very easy to learn . it is one of the best programing language .
  more programing languages c , c++ , java , ruby etc .''')
beforeLines = lines.split(".")
nowLines = lines.split(" ")
word = input("Enter what you want search : ").lower()
if word in nowLines:
    if word in str(beforeLines):
        for i in range(0, 5):
            if word in beforeLines[i]:
                # noSearchResult = 0
                # noSearchResult = noSearchResult + 1
                # print(f"{noSearchResult} Result found")
                print(beforeLines[i])

else:
    print("Sorry,\n\tNo result found")
