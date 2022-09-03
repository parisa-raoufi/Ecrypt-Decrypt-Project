
Message =  input("Enter our message =>   ")
Code=int (input("Enter code number that you want to use =>   "))
Mode=int(input("Enter 1 if you want ecrypt the message and if you want to decrypt the message, enter 2 pls =>   "))


def ecrypting(message , code):
    Length_Message = len(message)   
    NewMessage=""
    for letter in range(0 ,Length_Message) :
      FirstUniCodeLetter= ord(message[letter])     
      SeconderyUniCodeLetter= FirstUniCodeLetter + code
      Newlatter=chr(SeconderyUniCodeLetter)
      NewMessage=NewMessage+Newlatter
      
    print(NewMessage)



def decrypting(message , code):
    Length_Message = len(message)   
    NewMessage=""
    for letter in range(0 ,Length_Message) :
      FirstUniCodeLetter= ord(message[letter])     
      SeconderyUniCodeLetter= FirstUniCodeLetter - code
      Newlatter=chr(SeconderyUniCodeLetter)
      NewMessage=NewMessage + Newlatter
      
    print(NewMessage)

    

def CodeMassage (message , code , mode):
    if mode==1:
        ecrypting(message , code)
    elif mode==2:
        decrypting(message , code)
    else:
        mode = int(input("Pls just enter 1 or 0 => "))
        CodeMassage(message , code , mode)
    



CodeMassage(Message , Code , Mode)










