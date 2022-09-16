import Lexical

separator = []
puntuators = [';', ',', '\n', ':', '[', ']', '{', '}', '(', ')']
operators = ['and', 'or', 'not', '*', '/', '%', '+', '-', '<',
             '>', '>=', '<=', '!=', '==', '&&', '||', '!', '.']
assignments = ['+=', '-=', '++','--', '=']

separator.extend(puntuators)
separator.extend(assignments)
separator.extend(operators)

dot = '.'
space = ' '
quotes = ["'", '"']
commentOpen = '#*'
commentClose = '*#'
comments = [commentOpen, commentClose]


def BreakWord(string):
    lexeme = ''
    res = []
    i = 0
    dotcount = 0
    while (i < len(string)):
        character = string[i]
        if(character == '#' and string[i+1] == '*'):
            character += string[i+1]
            i += 1
        if character in comments:

            if i == len(string):
                break
            lexeme += character
            i += 1
            character = string[i]
            while(commentClose not in lexeme):
                lexeme += character
                if i == len(string)-1:
                    break
                i += 1
                character = string[i]
            if(i == len(string)):
                res.append(lexeme)
                lexeme = ''
                break
            character = string[i]
            res.append(lexeme)
            lexeme = ''
        if character in quotes:
            qouteIp = character
            if character == '\n':
                break
            lexeme += character
            i += 1
            character = string[i]
            while(character != qouteIp):
                if character == '\n':
                    break
                lexeme += character
                i += 1
                character = string[i]

            if(character == '\n'):
                res.append(lexeme)
                lexeme = ''

        if character != space:
            lexeme += character
        if i == len(string)-1:
            if character == space or character in separator or lexeme in separator:
                if lexeme != '':
                    res.append(lexeme)
                    lexeme = ''
            else:
                res.append(lexeme)
                lexeme = ''
        if (i+1 < len(string)):
            nextch = string[i+1]
            prech = string[i-1]

            if(nextch == '=')and(character in separator):
                lexeme += nextch
                i += 1
            if(nextch == dot):
                dotcount += 1
                i += 1
                character = string[i]
                nextch = string[i+1]
                if(Lexical.Alphabet(nextch) or len(lexeme) != 1 or nextch in separator):
                    res.append(lexeme)
                    lexeme = ''
                if(dotcount > 0):
                    lexeme += character

            if string[i+1] == space or string[i+1] in separator or lexeme in separator:
                if(character == '+'or character == '-'):
                    if(prech == '=' or prech == space or prech in operators):
                        if(string[i+1] != space):
                            i = i+1
                            character = string[i]
                            lexeme += character
                            while(character not in separator and string[i+1] not in separator and string[i+1] != space):
                                i = i+1
                                character = string[i]
                                lexeme += character
                if ((lexeme != '') and (dot not in lexeme)):
                    res.append(lexeme)
                    lexeme = ''
            if(nextch == ';' and lexeme):
                res.append(lexeme)
                lexeme = ''
            if character == dot and len(lexeme) == 1 and Lexical.Alphabet(nextch):
                res.append(lexeme)
                lexeme = ''
        i = i+1
    return res


