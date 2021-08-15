
def validate_brackets(str):
    string=list(str)
    brackets=['{','[','(']
    temp=[]

    for item in string:
        if item in brackets:
            temp+=[item]
        else:
            poped_val= temp.pop()
            if  poped_val== '(':
                if item != ")":
                    return False
            if poped_val == '{':
                if item != "}":
                    return False
            if poped_val == '[':
                if item != "]":
                    return False
            if temp:
                return False
            else:
                return True









if __name__=='__main__':

    print(validate_brackets('{}'))
    print(validate_brackets('{}(){}'))
    print(validate_brackets('()[[Extra Characters]]'))
    print(validate_brackets('(){}[[]]'))
    print(validate_brackets('{}{Code}[Fellows](())'))
    print(validate_brackets('[({}]'))
    print(validate_brackets('(]('))
    print(validate_brackets('{(})'))


