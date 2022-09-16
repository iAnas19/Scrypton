import Lexical
import Syntax

if __name__ == "__main__":
    TKs = Lexical.lexer('SAtest.txt')
    print('\n')
    i = 0
    print("---------------------------------------------------------------------------------------------------------------------")
    for T in TKs:
        print("Token: ", i, "\t\t\t", "Line: ", T.LineNumber, "\t\t\t",
              "Value: ", T.ValuePart, "\t\t\t", "Class", T.ClassPart)
        print("---------------------------------------------------------------------------------------------------------------------")
        i += 1
    Syntax.SA(TKs)
