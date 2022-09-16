import re
import WordBreak
import Token

FloatRegex =r"([+|-][0-9]*[.][0-9]+)|([0-9]*[.][0-9]+)"
StringRegex = r"[\w\W]*"
IdentifierRegex = r"(^[^\d\W]\w*\Z)"
IntegerRegex = r"[+|-][0-9]+"



Keywords =  ['int', 'float','array', 'string', 'boolean', 'for', 'while', 'is', 'in', 'if', 'else', 'else if', 'this',
 'extends', 'break', 'continue', 'true', 'false', 'none', 'class', 'post', 'userInput',
 'public', 'private', 'protected', 'function', 'return', 'main' 'and', 'or', 'not', 'mute',
 'try', 'catch']


def isKeyword(str1):
    if str1 in Keywords:
        return str1
    return ""


def isIdentifier(str1):
    pattern = re.compile(IdentifierRegex)
    if(re.fullmatch(pattern, str1)):
        return True


def isIntConstant(str1):
    pattern = re.compile(IntegerRegex)
    if(re.fullmatch(pattern, str1)):
        return True


def isFloatConstant(str1):
    pattern = re.compile(FloatRegex)
    if(re.fullmatch(pattern, str1)):
        return True


def isCharConstant(str1):
    pattern = re.compile(r"[\w\W]")
    if(re.fullmatch(pattern, str1)):
        return True


def isStringConstant(str1):
    pattern = re.compile(StringRegex)
    if(re.fullmatch(pattern, str1)):
        return True



digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

assignments = ['+=', '-=', '*=', '/=', '%=', '=']
MDM = ['*', '/', '%']
PM = ['+', '-']
ROP = ['<', '>', '>=', '<=', '!=', '==']
DataType = ['int', 'float', 'char', 'double', 'string']
AccessModifier = ['public', 'private', 'protected', 'sealed']


def lexer(filename):
    Tokens = []
    lineNo = 1
    string = readFile(filename)
    words = WordBreak.BreakWord(string)
    print(len(words))
    print(words)
    for word in words:
        Token1 = Token.Token()
        if ('\n' in word):
            lineNo += 1
        if('/*' in word):
            pass
        if(word[0] == '_'):
            if(isIdentifier(word)):
                Token1.CP = 'ID'
                Token1.VP = word
                Token1.LineNo = lineNo
                Tokens.append(Token1)
            else:
                Token1.CP = 'Invalid Lexeone'
                Token1.VP = word
                Token1.LineNo = lineNo
                Tokens.append(Token1)
                # word = ""

        if(isAlpha(word[0])):
            if(isIdentifier(word)):
                temp = isKeyword(word)
                if(temp == ""):
                    Token1.CP = 'ID'
                    Token1.VP = word
                    Token1.LineNo = lineNo
                    Tokens.append(Token1)
                    # word = ""
                else:
                    Token1.VP = temp
                    if(temp in DataType):
                        Token1.CP = 'DataType'
                    elif(temp in AccessModifier):
                        Token1.CP = 'AccessModifier'
                    else:
                        Token1.CP = temp
                        # Token1.VP = ""
                    Token1.LineNo = lineNo
                    Tokens.append(Token1)
                    # word = ""
            else:
                Token1.CP = 'Invalid Lexeone'
                Token1.VP = word
                Token1.LineNo = lineNo
                Tokens.append(Token1)
                # word = ""
        if(word in WordBreak.separator):
            if(word == '\n'):
                #Token1.CP = "CharConst"
                #Token1.VP = "LineBreak"
                #Token1.LineNo = lineNo
                # Tokens.append(Token1)
                # word = ""
                pass
            else:
                Token1.VP = word
                if(word in assignments):
                    Token1.CP = "AOP"
                elif(word in MDM):
                    Token1.CP = "MDM"
                elif(word in PM):
                    Token1.CP = "PM"
                elif(word in ROP):
                    Token1.CP = "ROP"
                else:
                    Token1.CP = word
                    # Token1.VP = ""
                Token1.LineNo = lineNo
                Tokens.append(Token1)
                # word = ""
        if(isDigit(word[0]) or ((word[0] == '+' or word[0] == '-') and (word not in WordBreak.separator))):
            if(isIntConstant(word)):
                Token1.CP = "int"
                Token1.VP = word
                Token1.LineNo = lineNo
                Tokens.append(Token1)
                # word = ""
            elif(isFloatConstant(word)):
                Token1.CP = "float"
                Token1.VP = word
                Token1.LineNo = lineNo
                Tokens.append(Token1)
                # word = ""
            else:
                Token1.CP = 'Invalid Lexeone'
                Token1.VP = word
                Token1.LineNo = lineNo
                Tokens.append(Token1)
                # word = ""
        if(word[0] in WordBreak.quotes):
            if(isStringConstant(word[1:-1])):
                if(len(word) == 3)or(len(word) == 4):
                    if(isCharConstant(word[1:-1])):
                        Token1.CP = "char"
                        Token1.VP = word[1:-1]
                        Token1.LineNo = lineNo
                        Tokens.append(Token1)
                        # word = ""
                else:
                    Token1.CP = "string"
                    Token1.VP = word[1:-1]
                    Token1.LineNo = lineNo
                    Tokens.append(Token1)
                    # word = ""
    Token11 = Token.Token()
    Token11.CP = "$"
    Token11.VP = '$'
    Token11.LineNo = lineNo
    Tokens.append(Token11)
    return Tokens


def readFile(filename):
    with open(filename, 'r') as myfile:
        data = myfile.read()
    return data


def isAlpha(ch):
    if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
        if(ch in WordBreak.puntuators):
            return False
        return True


def isDigit(ch):
    if(ch in digits):
        return True


