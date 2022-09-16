import re
import WordBreak
import Token

FloatRegex =r"([+|-][0-9]*[.][0-9]+)|([0-9]*[.][0-9]+)"
StringRegex = r"[\w\W]*"
IdentifierRegex = r"(^[^\d\W]\w*\Z)"
IntegerRegex = r"^[-+]?[0-9]+$"



Keywords =  ['int', 'float','array', 'string', 'boolean', 'for', 'while', 'is', 'in', 'if', 'else', 'else if', 'this',
 'extends', 'break', 'continue', 'true', 'false', 'none', 'class', 'post', 'userInput',
 'public', 'private', 'protected', 'function', 'return', 'main' 'and', 'or', 'not', 'mute',
 'try', 'catch']


def isKeyword(KeyW):
    if KeyW in Keywords:
        return KeyW
    return ""


def isIdentifier(ID):
    if(re.fullmatch(re.compile(IdentifierRegex), ID)):
        return True


def isInteger(INT):
    if(re.fullmatch(re.compile(IntegerRegex), INT)):
        return True


def isFloat(FLOAT):
    if(re.fullmatch(re.compile(FloatRegex), FLOAT)):
        return True

def isString(STR):
    if(re.fullmatch(re.compile(StringRegex), STR)):
        return True



digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

AssignmentOperator = ['+=', '-=', '*=', '/=', '%=', '=']
MDMAS = ['*', '/', '%','+', '-']
ROP = ['<', '>', '>=', '<=', '!=', '==']
DataType = ['int', 'float', 'double', 'string']
AccessModifier = ['public', 'private', 'protected', 'default']


def lexer(file):
    Tokens = []
    LineNumber = 1
    string = readFile(file)
    words = WordBreak.BreakWord(string)
    print(len(words))
    print(words)
    for word in words:
        Token1 = Token.Token()
        if ('\n' in word):
            LineNumber += 1
        if('/*' in word):
            pass
        if(word[0] == '_'):
            if(isIdentifier(word)):
                Token1.ClassPart = 'Identifier'
                Token1.ValuePart = word
                Token1.LineNumber = LineNumber
                Tokens.append(Token1)
            else:
                Token1.ClassPart = 'invalid'
                Token1.ValuePart = word
                Token1.LineNumber = LineNumber
                Tokens.append(Token1)

        if(Alphabet(word[0])):
            if(isIdentifier(word)):
                temp = isKeyword(word)
                if(temp == ""):
                    Token1.ClassPart = 'Identifier'
                    Token1.ValuePart = word
                    Token1.LineNumber = LineNumber
                    Tokens.append(Token1)
                else:
                    Token1.ValuePart = temp
                    if(temp in DataType):
                        Token1.ClassPart = 'DataType'
                    elif(temp in AccessModifier):
                        Token1.ClassPart = 'AccessModifier'
                    else:
                        Token1.ClassPart = temp
                    Token1.LineNumber = LineNumber
                    Tokens.append(Token1)
            else:
                Token1.ClassPart = 'invalid'
                Token1.ValuePart = word
                Token1.LineNumber = LineNumber
                Tokens.append(Token1)
                # word = ""
        if(word in WordBreak.separator):
            if(word == '\n'):
                pass
            else:
                Token1.ValuePart = word
                if(word in AssignmentOperator):
                    Token1.ClassPart = "AOP"
                elif(word in MDMAS):
                    Token1.ClassPart = "MDM"
                elif(word in ROP):
                    Token1.ClassPart = "ROP"
                else:
                    Token1.ClassPart = word
                Token1.LineNumber = LineNumber
                Tokens.append(Token1)
        if(isNumeral(word[0]) or ((word[0] == '+' or word[0] == '-') and (word not in WordBreak.separator))):
            if(isInteger(word)):
                Token1.ClassPart = "IntConst"
                Token1.ValuePart = word
                Token1.LineNumber = LineNumber
                Tokens.append(Token1)
            elif(isFloat(word)):
                Token1.ClassPart = "FloatConst"
                Token1.ValuePart = word
                Token1.LineNumber = LineNumber
                Tokens.append(Token1)
            else:
                Token1.ClassPart = 'invalid'
                Token1.ValuePart = word
                Token1.LineNumber = LineNumber
                Tokens.append(Token1)
        if(word[0] in WordBreak.quotes):
            if(isString(word[1:-1])):
                if(len(word) == 3)or(len(word) == 4):
                    if(isString(word[1:-1])):
                        Token1.ClassPart = "StringConst"
                        Token1.ValuePart = word[1:-1]
                        Token1.LineNumber = LineNumber
                        Tokens.append(Token1)
                else:
                    Token1.ClassPart = "StringConst"
                    Token1.ValuePart = word[1:-1]
                    Token1.LineNumber = LineNumber
                    Tokens.append(Token1)
    Token2 = Token.Token()
    Token2.ClassPart = "$"
    Token2.ValuePart = '$'
    Token2.LineNo = LineNumber
    Tokens.append(Token2)

    return Tokens

def readFile(file):
    with open(file, 'r') as myfile:
        data = myfile.read()
    return data


def Alphabet(ch):
    if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
        if(ch in WordBreak.puntuators):
            return False
        return True


def isNumeral(ch):
    return True if(ch in digits) else False


#                                                 ########################
        
