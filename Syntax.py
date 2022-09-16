# import regex
# import WordSplitter
from glob import glob
import Lexical

GI = 0

def ifstatment(TKs):
    global GI
    # GI=0
    if(TKs[GI].ClassPart == 'if'): 
        GI+=1
        # print("number",TKs[GI].LineNumber)
        if(TKs[GI].ClassPart == '('):
            GI+=1
            if(OE(TKs)):
                if(TKs[GI].ClassPart == ')'):
                    # # return True
                    GI+=1
                    if(TKs[GI].ClassPart == '{'):
                        GI+=1 
                        # return True
                        if body1(TKs):
                            # return True
                            if(TKs[GI].ClassPart == '}'):
                                GI+=1 
                                if elseifst(TKs):
                                # if(TKs[GI].ClassPart == ';'):
                                #     GI+=1
                                    return True
                            
                            # if elseif_st(TKs):
                            #     return True
    else:
        return False
def elseif_st(TKs):
    global GI
    if(elseifst(TKs)):
        if(elsest(TKs)):
            return True
    else:
        return True

def elseifst(TKs):
    global GI
    if(TKs[GI].ClassPart == 'elseif'): 
        GI+=1
        # print("number",TKs[GI].LineNumber)
        if(TKs[GI].ClassPart == '('):
            GI+=1
            if(OE(TKs)):
                if(TKs[GI].ClassPart == ')'):
                    # # return True
                    GI+=1
                    if(TKs[GI].ClassPart == '{'):
                        GI+=1 
                        # return True
                        if body1(TKs):
                            # return True
                            if(TKs[GI].ClassPart == '}'):
                                GI+=1 
                                if elseif_st(TKs):
                                # if(TKs[GI].ClassPart == ';'):
                                #     GI+=1
                                    return True
                            
    else:
        return True
def elsest(TKs):
    global GI
    if(TKs[GI].ClassPart == 'else'): 
        GI+=1
        # return True
        if(TKs[GI].ClassPart == '{'):
            GI+=1 
            # return True
            if body1(TKs):
                # return True
                if(TKs[GI].ClassPart == '}'):
                    GI+=1 
                    if(TKs[GI].ClassPart == ';'):
                        GI+=1
                        return True
    else:
        return True

def forst(TKs):
    global GI
    # forst_sel=['StringConst','IntConst','FloatConst']
    # forst_sel1=['++','--']
    if(TKs[GI].ClassPart == 'for'):
        GI+=1
        if(TKs[GI].ClassPart == '('):
            GI+=1
            if(TKs[GI].ClassPart == 'DataType'):
            # #     return True
            # # if(TKs[GI].ClassPart in forst_sel): 
                GI+=1
                if(TKs[GI].ClassPart == 'Identifier'):
                    GI+=1
                    if(TKs[GI].ClassPart == 'AOP'): 
                        if forst1(TKs):
                            return True
                    elif (TKs[GI].ClassPart == ';'):
                        if forst2(TKs):
                            return True

                        # if(TKs[GI].ClassPart == 'IntConst'):
                        #     GI+=1
                        # if(TKs[GI].ClassPart == ';'):
                        #     GI+=1
                        #     if(TKs[GI].ClassPart == 'Identifier'):
                        #         GI+=1
                        #         if(TKs[GI].ClassPart == 'ROP'):
                        #             GI+=1
                        #             if(TKs[GI].ClassPart == 'Identifier' or TKs[GI].ClassPart == 'IntConst'):
                        #                 GI+=1
                        #                 if(TKs[GI].ClassPart == ';'):
                        #                     GI+=1
                        #                     if(TKs[GI].ClassPart == 'Identifier'):
                        #                         GI+=1  
                        #                         if(TKs[GI].ClassPart in forst_sel1): 
                        #                             GI+=1
                        #                             if(TKs[GI].ClassPart == ')'):
                        #                         # if(TKs[GI].ClassPart == 'ROP'):   
                        #                                 return True
    else:
        return False

def forst1(TKs):
    global GI
    forst_sel1=['++','--'] 
    if(TKs[GI].ClassPart == 'AOP'):
        GI+=1
        if(TKs[GI].ClassPart == 'IntConst'):
            GI+=1
            if(TKs[GI].ClassPart == ';'):
                if forst2(TKs):
                    return True
                # if(TKs[GI].ClassPart == 'Identifier'):
                #     GI+=1
                #     if(TKs[GI].ClassPart == 'ROP'):
                #         GI+=1
                #         if(TKs[GI].ClassPart == 'Identifier' or TKs[GI].ClassPart == 'IntConst'):
                #             GI+=1
                #             if(TKs[GI].ClassPart == ';'):
                #                 GI+=1
                #                 if(TKs[GI].ClassPart == 'Identifier'):
                #                     GI+=1  
                #                     if(TKs[GI].ClassPart in forst_sel1): 
                #                         GI+=1
                #                         if(TKs[GI].ClassPart == ')'):
                #                             GI+=1
                #                     # if(TKs[GI].ClassPart == 'ROP'):   
                #                             return True

def forst2(TKs):
    global GI
    forst_sel1=['++','--']
    if(TKs[GI].ClassPart == ';'):
        GI+=1
        if(TKs[GI].ClassPart == 'Identifier'):
            GI+=1
            if(TKs[GI].ClassPart == 'ROP'):
                GI+=1
                if(TKs[GI].ClassPart == 'Identifier' or TKs[GI].ClassPart == 'IntConst'):
                    GI+=1
                    if(TKs[GI].ClassPart == ';'):
                        GI+=1
                        if(TKs[GI].ClassPart == 'Identifier'):
                            GI+=1  
                            if(TKs[GI].ClassPart in forst_sel1): 
                                GI+=1
                                if(TKs[GI].ClassPart == ')'):
                                    GI+=1
                                    if(TKs[GI].ClassPart == '{'):
                                        GI+=1 
                                        # return True
                                        if body1(TKs):
                                            # return True
                                            if(TKs[GI].ClassPart == '}'):
                                                GI+=1 
                                                return True
                                            # if(TKs[GI].ClassPart == 'ROP'):   
                                    

def whilest(TKs):
    global GI
    if(TKs[GI].ClassPart == 'while'):
        GI+=1 
        if(TKs[GI].ClassPart == '('):
            GI+=1 
            if OE(TKs):
                if(TKs[GI].ClassPart == ')'):
                    # return True
                    GI+=1
                    # return T
                    if(TKs[GI].ClassPart == '{'):
                        GI+=1 
                        # return True
                        if body1(TKs):
                            # return True
                            if(TKs[GI].ClassPart == '}'):
                                GI+=1 
                                return True
    else:
        return False
                
def body1(TKs):
    global GI
    Body1_sel = ['Identifier', 'this', 'while', 'if', 'for', 'return','function','DataType']
    if(TKs[GI].ClassPart in Body1_sel):  
        if(MST1(TKs)):
            return True
    else:
        return False
def MST1(TKs):
    global GI
    MST1_sel = ['Identifier', 'this', 'while', 'if', 'for', 'return','function','DataType']
    if(TKs[GI].ClassPart in MST1_sel):  
        if(SST1(TKs)):
            if(MST1(TKs)):
                return True
    else:
        return True
def SST1(TKs):
    global GI
    SST1_sel = ['Identifier', 'this', 'while', 'if', 'for', 'return','function','DataType']
    if(TKs[GI].ClassPart in SST1_sel):  
        # if(NewAssignSt(TKs)):
        #     return True
        # elif (NewDec(TKs)):
        #     return True
        if (whilest(TKs)):
            return True
        elif (RetSt(TKs)): 
            return True
        elif (forst(TKs)):
            return True
        elif (assignst_(TKs)):
            return True
        # elif (NewIncDecSt(TKs)):
            # return True
        elif (ifstatment(TKs)):
            return True
        elif (func(TKs)):
            return True
        else:
            return False
        
def Dec3(TKs):
    global GI
    type_sel=['StringConst','FloatConst','IntConst']
    if(TKs[GI].ClassPart in type_sel):
        GI+=1
        if Dec_(TKs):
            return True
    else:
        return False

def Dec_(TKs):
    global GI
    Dec_sel=['AOP',',',';']
    if(TKs[GI].ClassPart in Dec_sel):
        # GI+=1
        if(TKs[GI].ClassPart == 'AOP'):
            GI+=1
            if Dec3(TKs):
                return True
        if(TKs[GI].ClassPart == ','):
            GI+=1
            if Dec2(TKs):
                return True
            if Dec3(TKs):
                return True
        if(TKs[GI].ClassPart == ';'):
            GI+=1
            return True
        # if (Dec2(TKs)):
        #     return False
    else:
        return False
#3
def Dec2(TKs):
    global GI
    if(TKs[GI].ClassPart == 'Identifier'):
        GI+=1
        if(Dec_(TKs)):
            # if(Dec2(TKs)):
            return True
    else:
        return False
#1
def assignst_(TKs):
    global GI
    # GI = 0
    if(TKs[GI].ClassPart == 'DataType'): 
        GI +=1
        if(TKs[GI].ClassPart == 'Identifier'):
            GI += 1
            # return True
            if(Dec_(TKs)):
                return True
            # if(Dec2(TKs)):
            #     #return True
            #     if(Dec3(TKs)):      
            #         if(Dec_(TKs)):
            #             return True
    else:
        return False
# def func1(TKs):
#     global GI
#     func1_sel=['Identifier',',']
#     if(TKs[GI].ClassPart in func1_sel):
#         GI+=1
#         if(TKs[GI].ClassPart == ','): 
#             GI +=1 
#             if(TKs[GI].ClassPart == 'Identifier'): 
#                 GI +=1
#         elif func1(TKs):
#             return True
#     else:
#         return False

def func1(TKs):
    global GI
    if(TKs[GI].ClassPart == 'Identifier'):
            GI += 1
            if func2(TKs):
                return True
    else:
        return True
def func2(TKs):
    global GI
    if(TKs[GI].ClassPart == ','):
        GI += 1
        if(TKs[GI].ClassPart == 'Identifier'):
            GI += 1
            if func2(TKs):
                return True
    else:
        return True
def func(TKs):
    global GI
    # GI=0
    if(TKs[GI].ClassPart == 'function'):
        GI += 1
        if(TKs[GI].ClassPart == 'Identifier'):
            GI += 1
            if(TKs[GI].ClassPart == '('):
                GI+=1 
                # if(TKs[GI].ClassPart == 'Identifier'):
                #     GI += 1
                if func1(TKs):
                    # return True
                    if(TKs[GI].ClassPart == ')'):
                        GI+=1 
                        # return True
                        if(TKs[GI].ClassPart == '{'):
                            GI+=1 
                            # return True
                            if body1(TKs):
                                # return True
                                if(TKs[GI].ClassPart == '}'):
                                    GI+=1 
                                    return True
            
    else:
        return False



def NewIncDecSt(TKs):
    global GI
    if(TKs[GI].ClassPart == 'Identifier'):
        if(IncDec(TKs)):
            if(TKs[GI].ClassPart == ','):
                GI += 1
                return True
            return True
    else:
        return False

def IncDec(TKs):
    global GI
    if(TKs[GI].ClassPart=='Identifier'):
        if(FactorID(TKs)):
            return True
    else:
        return False       



def RetSt(TKs):
    global GI
    if(TKs[GI].ClassPart=='return'):
        GI+=1
        if(TKs[GI].ClassPart == '('):
            GI+=1 
            if OE(TKs):
                if(TKs[GI].ClassPart == ')'):
                    GI+=1
                    return True
    else:
        return False




def StaticOp(TKs):
    global GI
    StaticOp_sel = ['static', 'DT', 'tuple', 'Identifier', 'var']
    if(TKs[GI].ClassPart in StaticOp_sel):
        if(TKs[GI].ClassPart == 'static'):
            GI += 1
        return True
    else:
        return False

def AssignSt(TKs):
    global GI
    AssignSt_sel=['Identifier','this']
    if(TKs[GI].ClassPart in AssignSt_sel):
        if(FactorID(TKs)):
            return True
        elif(TKs[GI].ClassPart=='this'):
            GI+=1
            if(x(TKs)):
                if(Init(TKs)):
                    if(OEL(TKs)):
                        return True
    else:
        return False

def PLOpts(TKs):
    global GI
    PLOpts_sel=['static','DT', 'tuple', 'dict', 'Identifier', 'var', 'this', 'IntConst',
              'FloatConst', 'CharConst', 'StringConst', '(', 'not', 'True', 'False']
    if(TKs[GI].ClassPart in PLOpts_sel):
        if(Dec(TKs)):
            return True
        elif (OE(TKs)):
            return True
        elif(AssignSt(TKs)):
            return True
    else:
        return False
    
def PLOpts2(TKs):
    global GI
    PLOpts2_sel=['static','DT', 'tuple', 'dict', 'Identifier', 'var', 'this', 'IntConst',
              'FloatConst', 'CharConst', 'StringConst', '(', 'not', 'True', 'False']
    if(TKs[GI].ClassPart in PLOpts2_sel):
        if(PLOpts(TKs)):
            if(PL(TKs)):
                return True
            return True
    else:
        return False


def PL(TKs):
    global GI
    PL_sel = ['static', 'DT', 'tuple', 'dict', 'Identifier', 'var', 'this', 'IntConst',
              'FloatConst', 'CharConst', 'StringConst', '(', 'not', 'True', 'False', ',', ')']
    if(TKs[GI].ClassPart in PL_sel):
        if(PLOpts2(TKs)):
            if(TKs[GI].ClassPart == ','):
                GI += 1
                return True
        if(TKs[GI].ClassPart==')'):
            return True
    return False

def ToDec(TKs):
    global GI
    ToDec_sel = ['tuple', 'DT', 'dict', 'Identifier', 'var']
    if(TKs[GI].ClassPart in ToDec_sel):
        GI += 1
        return True
    return False


def xOpts(TKs):
    global GI
    xOpts_sel=['IntConst','AOP']
    if(TKs[GI].ClassPart in xOpts_sel):
        if(TKs[GI].ClassPart=='IntConst'):
            GI+=1
            return True
        return True
    else:
        return False

def Slice(TKs):
    global GI
    if(TKs[GI].ClassPart=='IntConst'):
        GI+=1
        if(TKs[GI].ClassPart==':'):
            GI+=1
            if(TKs[GI].ClassPart=='IntConst'):
                return True
    else:
        return False

def FactorBrackets(TKs):
    global GI
    FactorBrackets_sel=['IntConst',']']
    if(TKs[GI].ClassPart in FactorBrackets_sel):
        if(xOpts(TKs)):
            return True
        elif(Slice(TKs)):
            return True
    else:
        return False

def xOpts2(TKs):
    global GI
    xOpts2_sel=['Identifier','[','.','AOP']
    if(TKs[GI].ClassPart in xOpts2_sel):
        if(FactorID(TKs)):
            return True
        elif(x(TKs)):
            return True
    else:
        return False

def x(TKs):
    global GI
    x_sel=['[','.','AOP',',']
    if(TKs[GI].ClassPart in x_sel):
        if(TKs[GI].ClassPart=='['):
            GI+=1
            if(FactorBrackets(TKs)):
                if(TKs[GI].ClassPart==']'):
                    GI+=1
                    if(x(TKs)):
                        return True
        elif(TKs[GI].ClassPart=='.'):
            GI+=1
            if(xOpts2(TKs)):
                return True     
        return True
    else:
        return False

def StuffDic(TKs):
    global GI
    StuffDic_sel=['ID', 'IntConst','FloatConst', 'CharConst', 'StringConst','(', 'not', 'True', 'False',':']
    if(TKs[GI].ClassPart in StuffDic_sel):
        if(OE(TKs)):
            return True
        return True
    else:
        return False

def MoreDic(TKs):
    global GI
    MoreDic_sel=[',','}']
    if(TKs[GI].ClassPart in MoreDic):
        if(TKs[GI].ClassPart==','):
            GI+=1
            if(Dic(TKs)):
                return True
        return True
    else:
        return False

def Dic(TKs):
    global GI
    Dic_sel=['ID', 'IntConst','FloatConst', 'CharConst', 'StringConst','(', 'not', 'True', 'False',':']
    if(TKs[GI].ClassPart in Dic_sel):
        if(OE(TKs)):
            return True
        elif(StuffDic(TKs)):
            if(TKs[GI].ClassPart==':'):
                GI+=1
                if(StuffDic(TKs)):
                    if(MoreDic(TKs)):
                        return True
        return True
    else:
        return False

def TupleDec(TKs):
    global GI
    if(TKs[GI].ClassPart=='('):
        GI+=1
        if(OEL(TKs)):
            if(TKs[GI].ClassPart==')'):
                return True
    else:
        return False

def InitOpts(TKs):
    global GI
    InitOpts_sel=['ID', 'IntConst','FloatConst', 'CharConst', 'StringConst', '(','{','[','this', 'not', 'True', 'False']
    if(TKs[GI].ClassPart in InitOpts_sel):
        if(FactorID(TKs)):
            return True
        elif (OE(TKs)):
            return True
        elif(TKs[GI].ClassPart=='new'):
            GI+=1
            if(TKs[GI].ClassPart=='Identifier'):
                GI+=1
                if(TKs[GI].ClassPart=='('):
                    GI+=1
                    if(FactorBraces(TKs)):
                        if(TKs[GI].ClassPart==')'):
                            GI+=1
                            return True
        elif(Init(TKs)):
            return True
        elif(TKs[GI].ClassPart=='{'):
            GI+=1
            if(Dic(TKs)):
                if(TKs[GI].ClassPart=='}'):
                    Gi+=1
                    return True
        elif(TupleDec(TKs)):
            return True
        elif(TKs[GI].ClassPart=='['):
            GI+=1
            if(OEL(TKs)):
                if(TKs[GI].ClassPart==']'):
                    GI+=1
                    return True
        elif(TKs[GI].ClassPart=='this'):
            if(x(TKs)):
                return True
    else:
        return False

def Init(TKs):
    global GI
    Init_sel=['Identifier', 'IntConst',
             'FloatConst', 'CharConst', 'StringConst', '(', 'not', 'True', 'False','AOP',',']
    if(TKs[GI].ClassPart in Init_sel):
        if(TKs[GI].ClassPart=='AOP'):
            GI+=1
            if(InitOpts(TKs)):
                return True
        return True
    else:
        return False



def FI2Opts(TKs):
    global GI
    FI2Opts_sel=['Identifier', 'IntConst',
             'FloatConst', 'CharConst', 'StringConst', '(', 'not', 'True', 'False','static','DT','tuple','dict','var','this',',']
    if(TKs[GI].ClassPart in FI2Opts_sel):
        if(OEL2(TKs)):
            return True
    else:
        return False

def FactorID2(TKs):
    global GI
    FactorID2_sel = ['[', '.','AOP',',']
    if(TKs[GI].ClassPart in FactorID2_sel):
        if(x(TKs)):
            if(Init(TKs)):
                if(FI2Opts(TKs)):
                    return True
    else:
        return False

def FCOptsL(TKs):
    global GI
    FCOptsL_sel=['AOP','Identifier','IntConst','FloatConst','CharConst','StringConst','not','(','True','False']
    if(TKs[GI].ClassPart in FCOptsL_sel):
        if(Init(TKs)):
            if(OEL(TKs)):
                return True
        elif(OE(TKs)):
            if(OEL2(TKs)):
                return True

def FCOpts(TKs):
    global GI
    if(TKs[GI].ClassPart=='Identifier'):
        if(FactorID(TKs)):
            if(FCOptsL(TKs)):
                return True
    return False

def FactorComma(TKs):
    global GI
    if(TKs[GI].ClassPart==','):
        if(TKs[GI].ClassPart==','):
            GI+=1
            if(FCOpts(TKs)):
                return True
        return True
    else:
        return False

def OEL2(TKs):
    global GI
    if(TKs[GI].ClassPart==','):
        if(FactorComma(TKs)):
            return True
        return True
    else:
        return False

def OEL(TKs):
    global GI
    OEL_sel=['Identifier', 'IntConst',
             'FloatConst', 'CharConst', 'StringConst', '(', 'not', 'True', 'False']
    if(TKs[GI].ClassPart in OEL_sel):
        if(OE(TKs)):
            if(OEL2(TKs)):
                return True
        return True
    else:
        return False

def FactorBraces(TKs):
    global GI
    FactorBraces_sel = ['static', 'DT', 'tuple', 'dict', 'Identifier', 'var', 'this', 'IntConst',
                        'FloatConst', 'CharConst', 'StringConst', '(', 'not', 'True', 'False', ',', ')']
    if(TKs[GI].ClassPart in FactorBraces_sel):
        if(OEL(TKs)):
            return True
        elif (PL(TKs)):
            return True
        return True
    else:
        return False

def FnCall(TKs):
    global GI
    if(TKs[GI].ClassPart=='Identifier'):
        if(FactorID(TKs)):
            return True
    else:
        return False    



def T(TKs):
    global GI
    T_sel = ['Identifier', 'IntConst',
             'FloatConst', 'CharConst', 'StringConst', '(', 'not', 'True', 'False']
    if(TKs[GI].ClassPart in T_sel):
        if(TKs[GI].ClassPart=='Identifier'):
            GI+=1
            return True
        elif(TKs[GI].ClassPart=='IntConst' or TKs[GI].ClassPart=='FloatConst' or TKs[GI].ClassPart=='CharConst' or TKs[GI].ClassPart=='StringConst'):
            GI+=1
            return True
        elif(FnCall(TKs)):
            return True
        elif(TKs[GI].ClassPart=='('):
            GI+=1
            if(FnCall(TKs)):
                if(TKs[GI].ClassPart==')'):
                    GI+=1
                    return True
        elif(TKs[GI].ClassPart=='not'):
            GI+=1
            if(T(TKs)):
                return True
        elif(IncDec(TKs)):
            return True
        elif(TKs[GI].ClassPart=='True'):
            return True
        elif(TKs[GI].ClassPart=='False'):
            return True

def NT_(TKs):
    global GI
    NT__sel = ['static', 'DT', 'tuple', 'dict', 'Identifier', 'var', 'this', 'IntConst',
              'FloatConst', 'CharConst', 'StringConst', '(', 'not', 'True', 'False', ',', ')', ':', 'or', 'and', 'ROP', 'PM','MDM',';']
    if(TKs[GI].ClassPart in NT__sel):
        if(TKs[GI].ClassPart == 'MDM'):
            GI += 1
            if(T(TKs)):
                if(NT_(TKs)):
                    return True
        return True
    else:
        return False

def NT(TKs):
    global GI
    NT_sel = ['Identifier', 'IntConst',
             'FloatConst', 'CharConst', 'StringConst', '(', 'not', 'True', 'False']
    if(TKs[GI].ClassPart in NT_sel):
        if(T(TKs)):
            if(NT_(TKs)):
                return True
    else:
        return False

def E_(TKs):
    global GI
    E__sel = ['static', 'DT', 'tuple', 'dict', 'Identifier', 'var', 'this', 'IntConst',
              'FloatConst', 'CharConst', 'StringConst', '(', 'not', 'True', 'False', ',', ')', ':', 'or', 'and', 'ROP', 'PM',';']
    if(TKs[GI].ClassPart in E__sel):
        if(TKs[GI].ClassPart == 'PM'):
            GI += 1
            if(NT(TKs)):
                if(E_(TKs)):
                    return True
        return True
    else:
        return False


def E(TKs):
    global GI
    E_sel = ['Identifier', 'IntConst',
             'FloatConst', 'CharConst', 'StringConst', '(', 'not', 'True', 'False']
    if(TKs[GI].ClassPart in E_sel):
        if(NT(TKs)):
            if(E_(TKs)):
                return True
    else:
        return False


def RE_(TKs):
    global GI
    RE__sel = ['static', 'DT', 'tuple', 'dict', 'Identifier', 'var', 'this', 'IntConst',
               'FloatConst', 'CharConst', 'StringConst', '(', 'not', 'True', 'False', ',', ')', ':', 'or', 'and', 'ROP',';']
    if(TKs[GI].ClassPart in RE__sel):
        if(TKs[GI].ClassPart == 'ROP'):
            GI += 1
            if(E(TKs)):
                if(RE_(TKs)):
                    return True
        return True
    else:
        return False


def RE(TKs):
    global GI
    RE_sel = ['Identifier', 'IntConst',
              'FloatConst', 'CharConst', 'StringConst', '(', 'not', 'True', 'False']
    if(TKs[GI].ClassPart in RE_sel):
        if(E(TKs)):
            if(RE_(TKs)):
                return True
    else:
        return False


def AE_(TKs):
    global GI
    AE__sel = ['static', 'DT', 'tuple', 'dict', 'Identifier', 'var', 'this', 'IntConst',
               'FloatConst', 'CharConst', 'StringConst', '(', 'not', 'True', 'False', ',', ')', ':', 'or', 'and',';']
    if(TKs[GI].ClassPart in AE__sel):
        if(TKs[GI].ClassPart == 'and'):
            GI += 1
            if(RE(TKs)):
                if(AE_(TKs)):
                    return True
        return True
    else:
        return False


def AE(TKs):
    global GI
    AE_sel = ['Identifier', 'IntConst',
              'FloatConst', 'CharConst', 'StringConst', '(', 'not', 'True', 'False']
    if(TKs[GI].ClassPart in AE_sel):
        if(RE(TKs)):
            if(AE_(TKs)):
                return True
    else:
        return False


def OE_(TKs):
    global GI
    OE__sel = ['static', 'DT', 'tuple', 'dict', 'Identifier', 'var', 'this', 'IntConst',
               'FloatConst', 'CharConst', 'StringConst', '(', 'not', 'True', 'False', ',', ')', ':', 'or',';',]
    if(TKs[GI].ClassPart in OE__sel):
        if(TKs[GI].ClassPart == 'or'):
            GI += 1
            if(AE(TKs)):
                if(OE_(TKs)):
                    return True
        return True
    else:
        return False



def OE(TKs):
    global GI
    OE_sel = ['Identifier', 'IntConst',
              'FloatConst', 'CharConst', 'StringConst', '(', 'not', 'True', 'False']
    if(TKs[GI].ClassPart in OE_sel):
        if(AE(TKs)):
            if(OE_(TKs)):
                return True
    else:
        return False


def IncDecOp(TKs):
    global GI
    if(TKs[GI].ClassPart == 'AOP'):
        GI += 1
        return True


def FIOpts(TKs):
    global GI
    # print(GI)
    FIOpts_sel = ['AOP', '(', '[', '.',',','Identifier', 'IntConst',
              'FloatConst', 'CharConst', 'StringConst', '(', 'not', 'True', 'False',';',')']
    if(TKs[GI].ClassPart in FIOpts_sel):
        # GI += 1
        if(IncDecOp(TKs)):
            if(OE(TKs)):
                return True
        elif(TKs[GI].ClassPart == '('):
            GI += 1
            if(FactorBraces(TKs)):
                if(TKs[GI].ClassPart == ')'):
                    GI += 1
                    return True
        elif FactorID2(TKs):
            return True
        elif(OE(TKs)):
            return True
        return True
    else:
        return False


def FactorID(TKs):
    global GI
    if(TKs[GI].ClassPart == 'Identifier'):
        GI += 1
        # print(GI)
        if(FIOpts(TKs)):
            return True
    return False


def Dec(TKs):
    global GI
    Dec_sel = ['static', 'tuple', 'DT', 'dict', 'Identifier', 'var']
    if(TKs[GI].ClassPart in Dec_sel):
        if(StaticOp(TKs)):
            if(ToDec(TKs)):
                if(FactorID(TKs)):
                    return True
    return False


def Start(TKs):
    global GI
    GI = 0
    # Start_sel = ['def', 'public', 'private', 'protected', 'sealed', 'static',
    #              'abstract', 'class', 'DT', 'tuple', 'dict', 'Identifier', 'var','main']
    Start_sel = ['if','for','while','funtion','Identifier','return','DataType']
    if(TKs[GI].ClassPart in Start_sel):
        if(MST1(TKs)):
            return True
        # print(GI)
        # if(Defs(TKs)):
        #     if(TKs[GI].ClassPart == 'main'):
        #         GI += 1
        #         if(TKs[GI].ClassPart == '('):
        #             GI += 1
        #             if(TKs[GI].ClassPart == ')'):
        #                 GI += 1
        #                 if(TKs[GI].ClassPart == '{'):
        #                     GI += 1
        #                     if(MST(TKs)):
        #                         if(TKs[GI].ClassPart == '}'):
        #                             GI += 1
        #                             if(Defs(TKs)):
        #                                 return True
        # return True
    else:
        return False

                                            
def SA(TKs):
    global GI
    if(Start(TKs)):
        print("Valid Syntax")
    else:
        print("Syntax Error at Line Number ", TKs[GI].LineNumber-1)