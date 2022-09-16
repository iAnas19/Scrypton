import Lexical
import WordBreak


# txt = 'my name is "15.23\n12.ab6.24'
# bla = WordBreak.BreakWord(txt)
# print(bla)


if __name__ == "__main__":
    TKs = Lexical.lexer('code.txt')
    print("total tokens in the code: ", len(TKs))
    i = 0
    for T in TKs:
            print("Token number "+str(i))
            print("Line: "+str(T.LineNo))
            print("Value: "+T.VP)
            print("Class: "+T.CP)

            print("\n")
            i += 1

# with open("tokens5.txt", "a") as myfile:
#     for T in TKs:
#         myfile.write("Token "+str(i)+":")
#         myfile.write("\n")
#         myfile.write("Class: "+T.CP)
#         myfile.write("\n")
#         myfile.write("Value: "+T.VP)
#         myfile.write("\n")
#         myfile.write("Line: "+str(T.LineNo))
#         myfile.write("\n")
#         myfile.write("\n")
#         myfile.write("\n")
#         i += 1

