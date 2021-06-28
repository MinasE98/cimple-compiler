'''
AM : 4244 Marios Gavriil , username :cse74244
AM : 4245 Minas Eleftheriou , username :cse74245
'''
import os
import sys
characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
              'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

file = open(sys.argv[1], 'r')
file_extension= os.path.splitext(sys.argv[1])
if(file_extension[1]=='.ci'):
    pass
else:
    print('File must be of type.ci')
    exit(1)

start = 0
dig = 1
idk = 2
asgn = 3
smaller = 4
greater= 5
rem = 6


white_character = 0
character = 1
digit = 2
real_op_less = 3
real_op_more = 4
real_op_equal = 5
mult_op_multiply = 6
mult_op_divide = 7
add_op_add = 8
add_op_sub = 9
coma = 10
semi_colon = 11
left_parenthesis = 12
right_parethensis = 13
left_bracket = 14
right_bracket = 15
open_code_block = 16
close_code_block = 17
EoF = 18
not_acceptable_character = 19
change_of_line = 20
colon = 21
full_stop = 22
comment = 23


identifier_token = 100
digit_token = 101
real_op_less_token = 102
real_op_more_token = 103
real_op_equal_token = 104
real_op_lessEq_token = 105
real_op_moreEq_token = 106
notEqual_token = 107
mul_op_multiply_token = 108
mul_op_divide_token = 109
add_op_add_token = 110
add_op_sub_token = 111
coma_token = 112
semi_colon_token = 113
left_parathensis_token = 114
right_parenthesis_token = 115
left_bracket_token = 116
right_bracket_token = 117
open_code_block_token = 118
close_code_block_token = 119
EoF_token = 120
colon_token = 121
assign_token = 122
full_stop_token = 123
program_token = 124
declare_token = 125
if_token = 126
else_token = 127
while_token = 128
switchcase_token = 129
incase_token = 130
forcase_token = 131
case_token = 132
default_token = 133
procedure_token = 134
function_token = 135
call_token = 136
return_token = 137
in_token = 138
inout_token = 139
and_token = 140
or_token = 141
not_token = 142
input_token = 143
print_token = 144
error_not_acceptable_character = 145
error_on_potential_number = 146
error_on_assign = 147
error_number_out_of_bounds = 148
error_over_30_char = 149
error_EoF_in_comments = 150
error_full_stop=151
boundary_words = ['program', 'declare', 'if', 'else', 'while', 'switchcase', 'forcase', 'incase', 'default', 'case',
                      'not', 'and', 'or','function', 'procedure', 'call', 'return', 'in', 'inout','input', 'print']

DictOfStrTokens={   100:'Identifier',101:'Digit',102:'Less Operator',103:'More Operator',104:'Equal Operator',
                    105:'Less or Equal Operator',106:'More or Equal Operator',107:'Not Equal Operator',108:'Multiply Operator',
                    109:'Divide Operator',110:'Addition Operator',111:'Sub Operator',112:'Coma Operator',
                    113:'Semi Colon Operator',114:'Left Parenthesis Operator',115:'Right Parenthesis Operator',
                    116:'Left Bracket Operator',117:'Right Bracket Operator',118:'Open Block Code ',
                    119:'Close Block Code',120:'EoF',121:'Colon Operator ',122:'Assign Operator',
                    123:'FullStop Operator',124:'Program Operator',125:'Declare Operator',126:'If Operator',
                    127:'Else Operator',128:'While Operator',129:'SwitchCase Operator',130:'InCase Operator',
                    131:'ForCase Operator',132:'Case Operator',133:'Default Operator',134:'Procedure Operator',
                    135:'Function Operator' ,136:'Call Operator',137:'Return Operator',138:'In Operator',139:'InOut Operator',
                    140:'And Operator',141:'Or Operator',142:'Not Operator',143:'Input Operator',144:'Print Operator',
                    145:'Error:Not Accepptable Character',146:'Error:On Potential Number(Character after Digit)',
                    147:'Error:On Assign',148:'Error:Number out of bounds',149:'Error:Identifier more than 30 characters',
                    150:'Error:EoF between comments',151:'Error : FullStop should only be use to close your program,its not acceptable as a character anywhere else(except in comments!)'}

# 0->Start, 1->dig , 2->idk , 3->asgn , 4->smaller , 5->greater , 6->rem
#Efarmozoume to aftomato os pinaka 2 diastaseon opou TableOfStates[katastasis][simvolo] 

TableOfStates =[
    #0
    [start, idk, dig, smaller, greater, real_op_equal_token, mul_op_multiply_token,
     mul_op_divide_token, add_op_add_token, add_op_sub_token, coma_token, semi_colon_token, left_parathensis_token, right_parenthesis_token, left_bracket_token,
     right_bracket_token, open_code_block_token, close_code_block_token, EoF_token, not_acceptable_character, start, asgn,
     full_stop_token, rem],
    #1
    [digit_token, error_on_potential_number, dig, digit_token, digit_token, digit_token, digit_token, digit_token, digit_token,
     digit_token, digit_token, digit_token, digit_token, digit_token, digit_token, digit_token, digit_token, digit_token,
     digit_token,error_not_acceptable_character , digit_token, digit_token, error_full_stop, digit_token],
    #2
    [identifier_token, idk, idk, identifier_token, identifier_token, identifier_token, identifier_token, identifier_token,
     identifier_token, identifier_token, identifier_token, identifier_token, identifier_token, identifier_token,
     identifier_token, identifier_token, identifier_token, identifier_token, identifier_token, error_not_acceptable_character,
     identifier_token, identifier_token, error_full_stop, identifier_token],
    #3
    [error_on_assign, error_on_assign, error_on_assign, error_on_assign, error_on_assign,
     assign_token, error_on_assign, error_on_assign, error_on_assign, error_on_assign,
     error_on_assign, error_on_assign, error_on_assign, error_on_assign, error_on_assign,
     error_on_assign, error_on_assign, error_on_assign, error_on_assign, error_on_assign,
     error_on_assign, error_on_assign, error_on_assign, error_on_assign],
    #4
    [real_op_less_token, real_op_less_token, real_op_less_token, real_op_less_token, notEqual_token, real_op_lessEq_token, real_op_less_token, real_op_less_token,
     real_op_less_token, real_op_less_token, real_op_less_token, real_op_less_token, real_op_less_token, real_op_less_token, real_op_less_token, real_op_less_token, real_op_less_token,
     real_op_less_token, real_op_less_token, error_not_acceptable_character, real_op_less_token, real_op_less_token, real_op_less_token, real_op_less_token],
    #5
    [real_op_more_token, real_op_more_token, real_op_more_token, real_op_more_token, real_op_more_token, real_op_moreEq_token, real_op_more_token,
     real_op_moreEq_token, real_op_more_token, real_op_more_token, real_op_more_token, real_op_more_token, real_op_more_token, real_op_more_token,
     real_op_more_token, real_op_more_token, real_op_more_token, real_op_more_token, real_op_more_token, error_not_acceptable_character,real_op_more_token, real_op_more_token, error_full_stop, real_op_more_token],
    #6
    [rem, rem, rem, rem, rem, rem, rem, rem, rem, rem, rem, rem, rem, rem, rem, rem, rem, rem, error_EoF_in_comments, rem, rem, rem,
     rem, start]

]
def charactercheck(c,counter):
    result=[]
    if (c == ' ' or c == '\t'):
        Temp_token = white_character
    elif (c in characters):
        Temp_token = character
    elif (c in digits):
        Temp_token = digit
    elif (c == '<'):
        Temp_token = real_op_less
    elif (c == '>'):
        Temp_token = real_op_more
    elif (c == '='):
        Temp_token = real_op_equal
    elif (c == '*'):
        Temp_token = mult_op_multiply
    elif (c == '/'):
        Temp_token = mult_op_divide
    elif (c == '+'):
        Temp_token = add_op_add
    elif (c == '-'):
        Temp_token = add_op_sub
    elif (c == ','):
        Temp_token = coma
    elif (c == ';'):
        Temp_token = semi_colon
    elif (c == '('):
        Temp_token = left_parenthesis
    elif (c == ')'):
        Temp_token = right_parethensis
    elif (c == '['):
        Temp_token = left_bracket
    elif (c == ']'):
        Temp_token = right_bracket
    elif (c == '{'):
        Temp_token = open_code_block
    elif (c == '}'):
        Temp_token = close_code_block
    elif (c == ''):
        Temp_token = EoF
    elif (c == '\n'):
        counter = counter + 1
        Temp_token = change_of_line
    elif (c == ':'):
        Temp_token = colon
    elif (c == '.'):
        Temp_token = full_stop
    elif (c == '#'):
        Temp_token = comment
    else:
        Temp_token = not_acceptable_character
    result.append(Temp_token)
    result.append(counter)
    return result;
def boundedWordCheck(token_word):
    if (token_word == 'program'):
        state = program_token
    elif (token_word == 'declare'):
        state = declare_token
    elif (token_word == 'if'):
        state = if_token
    elif (token_word == 'else'):
        state = else_token
    elif (token_word == 'while'):
        state = while_token
    elif (token_word == 'switchcase'):
        state = switchcase_token
    elif (token_word == 'forcase'):
        state = forcase_token
    elif (token_word == 'incase'):
        state = incase_token
    elif (token_word == 'case'):
        state = case_token
    elif (token_word == 'default'):
        state = default_token
    elif (token_word == 'procedure'):
        state = procedure_token
    elif (token_word == 'inout'):
        state = inout_token
    elif (token_word == 'and'):
        state = and_token
    elif (token_word == 'or'):
        state = or_token
    elif (token_word == 'not'):
        state = not_token
    elif (token_word == 'input'):
        state = input_token
    elif (token_word == 'function'):
        state = function_token
    elif (token_word == 'call'):
        state = call_token
    elif (token_word == 'return'):
        state = return_token
    elif (token_word == 'in'):
        state = in_token
    elif (token_word == 'print'):
        state = print_token
    return state
def errorCheck(state,counter):
    if (state == error_not_acceptable_character):
        print(DictOfStrTokens.get(error_not_acceptable_character),'on line :',counter)
        exit(1)
    elif (state == error_on_potential_number):
        print(DictOfStrTokens.get(error_on_potential_number),'on line :',counter)
        exit(1)
    elif (state == error_on_assign):
        print(DictOfStrTokens.get(error_on_assign),'on line :',counter)
        exit(1)
    elif (state == error_number_out_of_bounds):
        print(DictOfStrTokens.get(error_number_out_of_bounds),'on line :',counter)
        exit(1)
    elif (state == error_EoF_in_comments):
        print(DictOfStrTokens.get(error_EoF_in_comments),'on line :',counter)
        exit(1)
    elif (state == error_over_30_char):
        print(DictOfStrTokens.get(error_over_30_char),'on line :',counter)
        exit(1)
    elif(state == error_full_stop):
        print(DictOfStrTokens.get(error_full_stop),', on line :',counter)
        exit(1)
getlines = 1
def lex():
    global getlines
    global DictOfStrTokens
    token_word = ''
    state = start
    resultTable=[]
    counter = getlines
    while (state >= 0 and state <= 6):
        c = file.read(1)
        result = charactercheck(c,counter)
        Temp= result[0]
        counter=result[1]
        state = TableOfStates[state][Temp]
        if (len(token_word) < 30):
            if (state != start and state != rem):
                token_word += c
        else:
            state = error_over_30_char
    if (state == identifier_token or state == digit_token or state == real_op_less_token or state == real_op_more_token):
        if (c == '\n'):
            counter -= 1
        c = file.seek(file.tell() - 1, 0)
        token_word = token_word[:-1]
    if (state == identifier_token):
        if (token_word in boundary_words):
            state=boundedWordCheck(token_word)
    if (state == digit_token):
        if (token_word.isdigit() >= pow(2, 32)):
            state = error_number_out_of_bounds
    errorCheck(state,counter)
    StrofCurrent = DictOfStrTokens.get(state)
    resultTable.append(StrofCurrent)
    resultTable.append(state)
    resultTable.append(token_word)
    resultTable.append(counter)
    getlines = counter
    return resultTable

global generalList
global tableOfTemps
global tempListDec
tempListDec=[]
tableOfTemps=[]
generalList = []
resultList=[]
getQuadId=101
TempVar=1
def genQuad(Op,x,y,z):
    global generalList
    global getQuadId
    global generalList
    global resultList
    tempList=[]
    tempList+=[nextQuad()]+[Op]+[x]+[y]+[z]
    generalList+=[tempList]
    resultList+=[tempList]
    getQuadId+=1
    return tempList

def nextQuad():
    global getQuadId
    return getQuadId

def newTemp():
	#creating temporary variables
    global TempVar
    global tableOfTemps
    x='T_'
    createTemp=x+str(TempVar)
    TempVar+=1
    tableOfTemps+=[createTemp]
    #creating a new entity for each new temp variable
    entity = Entity()
    entity.type="TEMP"
    entity.name= createTemp
    entity.TempVar.offset=compute_offset()
    add_entities(entity)
    return createTemp

def emptyList():
    tagList=[]
    return tagList

def makeList(x):
    makeListTable=[x]
    return makeListTable

def merge(list1,list2):
    mergeListTable=[]
    mergeListTable+=list1+list2
    return mergeListTable

def backPatch(list,z):
    global generalList
    for i in range(len(list)) :
        for j in range(len(generalList)):
            if (list[i]==generalList[j][0] and generalList[j][4]=='_'):
                generalList[j][4]=z
                break;
    return 
class Scope():
	def __init__(self):
		self.scope_name=""
		self.entityList=[]
		self.scope_lvl=0
		self.parent_scope=None
class Entity():
	def __init__(self):
		self.name = ""
		self.type = ""
		self.var = self.Var()
		self.subprogram = self.Subprogram()
		self.parameter = self.Parameter()
		self.TempVar = self.TempVar()
	class Var():
		def __init__(self):
			self.offset=0
	class Subprogram():
		def __init__(self):
			self.startQuad = 1
			self.frameLength=0
			self.argumentList=[]
	class Parameter():
		def __init__(self):
			self.par_mode =""
			self.offset=0		
	class TempVar():
		def __init__(self):
			self.offset = 0
class Argument():
	def __init__(self):
		self.arg_name = ""
		self.parMode=""
current_scope=None
scope_list=[]
printing_scope_list=[]
def add_scope(scope):
	# creating a new list containing all scopes 
	global scope_list
	global printing_scope_list
	global current_scope
	global first_scope
	new_scope=Scope()
	new_scope.scope_name=scope
	new_scope.parent_scope=current_scope
	# if its the first scope aka the main program the scope level is 0
	if (len(scope_list)==0):
		first_scope=new_scope
		new_scope.scope_lvl=0
	else:
	#if its not the first then the scope_lvl is equal to the size of the list
		new_scope.scope_lvl = len(scope_list)
	#setting as the current scope the new scope we created
	current_scope=new_scope
	scope_list.append(new_scope)
	printing_scope_list.append(new_scope)
														
def add_entities(entity):
	global current_scope
	# adding a new entity into the entityList of out current _scope
	current_scope.entityList.append(entity)

def add_arguments(argument):
	global current_scope
	#adding a new argument into the argumentList of the current entity(the last one) 
	current_scope.entityList[-1].subprogram.argumentList.append(argument)

def pass_parameters():
	#each argument in the argument list must be passed to the next scope aka the new subprogram(last entity in the entity list) as parameters so we create them
	global current_scope
	for argument in current_scope.parent_scope.entityList[-1].subprogram.argumentList:
		new_ent=Entity()
		new_ent.name=argument.name
		new_ent.type="PARAM"
		new_ent.parameter.par_mode=argument.parMode
		new_ent.parameter.offset=compute_offset()
		add_entities(new_ent)

def compute_offset():
	#to compute the offset in the current scope if there is an entity inside the entity list we go through the entityList and for each entity that is not a subprogram 
	global current_scope
	counter=0
	offset=0
	if (len(current_scope.entityList)!=0):
		for entity in (current_scope.entityList):
			if(entity.type!="SUBPR"):
				counter+=4
	offset=12+counter
	return offset
	
Fname=sys.argv[1]
Fname=Fname.replace(".ci","")
Fname+=".txt"
symbols = open(Fname,'w')

def print_Symbols():
	#printing the symbols table
	global current_scope
	symbols.write("Scope_name: "+current_scope.scope_name+" scope_lvl: "+str(current_scope.scope_lvl)+"\n")
	symbols.write("\nEntities:[  ")
	for ent in current_scope.entityList:
		symbols.write(" "+ent.name+"  ")
	symbols.write("]\n\n")
	for ent in current_scope.entityList:
		if(ent.type == 'PARAM'):
			symbols.write("Entity_name: "+ent.name+"  type: "+ent.type+"  mode: "+ent.parameter.par_mode+"  offset: "+str(ent.parameter.offset)+"\n")
		elif(ent.type == 'VAR'):
			symbols.write("Entity_name: "+ent.name+"  entity_type: "+ent.type+"  variable-type: Int  offset: "+str(ent.var.offset)+"\n")
		elif(ent.type == 'TEMP'): 
			symbols.write("Entity_name: "+ent.name+"  entity_type: "+ent.type+"  offset: "+str(ent.TempVar.offset)+"\n")
		elif(ent.type == 'SUBPR'):
			symbols.write("Entity_name: "+ent.name+"  entity_type:"+ent.type+"  function-type:"+ent.subprogram.type+"  startQuad:"+str(ent.subprogram.startQuad)+"  frameLength:"+str(ent.subprogram.frameLength)+"\n")
			if (len(ent.subprogram.argumentList)!=0):
				symbols.write("Arguments for "+ent.name+"\n")
				for arg in ent.subprogram.argumentList:
					symbols.write("   Argument_name: "+arg.name+"  type : Int  parMode:"+arg.parMode+"\n")
		symbols.write("\n")
#searching for an entity in all scopes 
def search(n):
	global current_scope
	global first_scope
	scope=current_scope
	for scope in scope_list:
		for entity in scope.entityList:
			if(entity.name == n):
				return (scope,entity)
	for entity in first_scope.entityList:
		if(entity.name==n):
			return(first_scope,entity)
	return(0,0)

#creating the file to write the final code
Fname=sys.argv[1]
Fname=Fname.replace(".ci","")
Fname+=".asm"
final_code=open(Fname,"w")

def storerv(r,v):
	global current_scope
	(sc,en)=search(v)
	#if v is variable declared in the main program
	if en.type == "VAR" and sc.scope_lvl==0 :
		final_code.write("sw "+r+",-"+str(en.var.offset)+"($s0)\n")
	#if v is a temporary variable in the main program
	elif en.type == "TEMP" and sc.scope_lvl==0 :
		final_code.write("sw "+r+",-"+str(en.TempVar.offset)+"($s0)\n")
	#if  v is a variable in the current scope 
	elif en.type=="VAR" and sc.scope_lvl==current_scope.scope_lvl:
		final_code.write("sw "+r+",-"+str(en.var.offset)+"($sp)\n")
	#if v a temporary variable in the current scope
	elif en.type=="TEMP" and sc.scope_lvl==current_scope.scope_lvl:
		final_code.write("sw "+r+",-"+str(en.TempVar.offset)+"($sp)\n")
	#if v a parameter pass with value and is in the current scope
	elif en.type=="PARAM" and en.parameter.par_mode=="CV" and sc.scope_lvl==current_scope.scope_lvl:
		final_code.write("sw "+r+",-"+str(en.parameter.offset)+"($sp)\n")
	#if  v is a parameter pass with reference in the current scope 
	elif en.type=="PARAM" and en.parameter.par_mode=="REF" and sc.scope_lvl==current_scope.scope_lvl:
		final_code.write("lw $t0,-"+str(en.parameter.offset)+"($sp)\nsw "+r+",($t0)\n")
	#if v is a variable and is declared in a parent scope
	elif en.type == "VAR" and sc.scope_lvl < current_scope.scope_lvl:
		gnlvcode(v)
		final_code.write("sw "+r+",($t0)\n")
	#if v is a parameter passed with value declared in a parent scope
	elif en.type=="PARAM" and en.parameter.par_mode=="CV"and sc.scope_lvl < current_scope.scope_lvl:
		gnlvcode(v)
		final_code.write("sw "+r+",($t0)\n")
	#if v is a parameter passed with reference declared in a parent scope 
	elif en.type=="PARAM" and en.parameter.par_mode=="REF"and sc.scope_lvl < current_scope.scope_lvl:
		gnlvcode(v)
		final_code.write("lw $t0,($t0)\nsw "+r+",($t0)\n")

def gnlvcode(name):
	global current_scope
	global scope_list
	(sc,en)=search(name)
	#finding the level if the variable 
	final_code.write("lw $t0,-4($t0)\n")
	#we are subtracting 1 level because we already made the stack of the parent
	myrange=current_scope.scope_lvl-sc.scope_lvl-1
	for i in range(0,myrange):
		final_code.write("lw $t0,-4($t0)\n")
	#finding the offset of the variable or parameter
	if en.type=="VAR":
		off=en.var.offset
	else  :
		off=en.parameter.offset
	#adding the address of the var
	final_code.write("addi $t0,$t0,-"+str(off)+"\n")

def loadvr(v,r):
	global current_scope
	#if v is a number 
	if v.isdigit():
		final_code.write("li "+r+","+str(v)+"\n")
	else:
		(sc,en)=search(v)
		#if v its a variable and is inside the main program
		if en.type=="VAR" and sc.scope_lvl==0 :
			final_code.write("lw "+r+",-"+str(en.var.offset)+"($s0)\n")
		#if v its a temporary variable we created and is inside the main program			
		elif en.type=="TEMP" and sc.scope_lvl==0 :
			final_code.write("lw "+r+",-"+str(en.TempVar.offset)+"($s0)\n")
		#for the next 3 elif if v is a variable or a temporary variable or is a parameter passed with value and is inside the  scope we currently are
		elif en.type=="VAR" and sc.scope_lvl==current_scope.scope_lvl:
			final_code.write("lw "+r+",-"+str(en.var.offset)+"($sp)\n")
		elif en.type=="TEMP" and sc.scope_lvl==current_scope.scope_lvl:
			final_code.write("lw "+r+",-"+str(en.TempVar.offset)+"($sp)\n")
		elif en.type=="PARAM" and en.parameter.par_mode=="CV" and sc.scope_lvl==current_scope.scope_lvl:
			final_code.write("lw "+r+",-"+str(en.parameter.offset)+"($sp)\n")
		#if v is a parrameter passed with reference
		elif en.type=="PARAM" and en.parameter.par_mode=="REF"and sc.scope_lvl==current_scope.scope_lvl:
			final_code.write("lw $t0,-"+str(en.parameter.offset)+"($sp)\nlw "+r+",($t0)\n")
		#if  v has been declared in a parent scope and is a variable or a prameter passed with value
		elif (sc.scope_lvl<current_scope.scope_lvl and en.type=="VAR") or (sc.scope_lvl<current_scope.scope_lvl and en.type=="PARAM" and en.parameter.par_mode=="CV"):
			gnlvcode(v)
			final_code.write("lw "+r+",($t0)\n")
		#if v has been declared in a parent  and is  a parameter passed with reference
		elif sc.scope_lvl<current_scope.scope_lvl and en.type=="PARAM" and en.parameter.par_mode=="REF":
			gnlvcode(v)
			final_code.write("lw $t0,($t0)\nlw "+r+"($t0)\n")	
#removing the scope from the scopeList
def close_scope():
	global current_scope
	global scope_list
	closed_scope = current_scope
	current_scope=current_scope.parent_scope
	scope_list.remove(closed_scope)
#here we generate the final code by going through the generalList 
def final():
	global current_scope
	global generalList
	global first_scope
	parCounter=0
	for i in range(len(generalList)):
		#because the main is not always the first we create a space so the jump to the main must be written
		if (generalList[i][0]==101):
			final_code.write("\n\n\n\n\n\n\n\nL"+str(generalList[i][0])+":\n\n")
		else:
			final_code.write("L"+str(generalList[i][0])+":\n\n")
		#JUMP
		if (generalList[i][1] == 'jump'):
			final_code.write('b L'+str(generalList[i][4])+"\n")
		#EQUAL
		elif (generalList[i][1] == '='):
			loadvr(generalList[i][2],"$t1")
			loadvr(generalList[i][3],"$t2")
			final_code.write('beq,$t1,$t2,L'+str(generalList[i][4])+"\n")
		#LESS THAN
		elif (generalList[i][1] == '<'): 
			loadvr(generalList[i][2],"$t1")
			loadvr(generalList[i][3],"$t2")
			final_code.write('blt,$t1,$t2,L'+str(generalList[i][4])+"\n")
		#GREATER THAN
		elif (generalList[i][1] == '>'): 
			loadvr(generalList[i][2],"$t1")
			loadvr(generalList[i][3],"$t2")
			final_code.write('bgt,$t1,$t2,L'+str(generalList[i][4])+"\n")
		#LESS OR EQUAL
		elif (generalList[i][1] == '<='): 
			loadvr(generalList[i][2],"$t1")
			loadvr(generalList[i][3],"$t2")
			final_code.write('ble,$t1,$t2,L'+str(generalList[i][4])+"\n")
		#GREATER OR EQUAL
		elif (generalList[i][1] == '>='):	
			loadvr(generalList[i][2],"$t1")
			loadvr(generalList[i][3],"$t2")
			final_code.write('bge,$t1,$t2,L'+str(generalList[i][4])+"\n")
		#DIFFERENT
		elif (generalList[i][1] == '<>'): 
			loadvr(generalList[i][2],"$t1")
			loadvr(generalList[i][3],"$t2")
			final_code.write('bne,$t1,$t2,L'+str(generalList[i][4])+"\n")	
		#ASSIGNATION
		elif (generalList[i][1] == ':='): 
			loadvr(generalList[i][2],"$t1")
			storerv("$t1",generalList[i][4])
		#ADDITION
		elif (generalList[i][1] == '+'): 
			loadvr(generalList[i][2],"$t1")
			loadvr(generalList[i][3],"$t2")
			final_code.write('add,$t0,$t1,$t2'+"\n")
			storerv("$t1",generalList[i][4])
		#SUBTRACTION
		elif (generalList[i][1] == '-'): 
			loadvr(generalList[i][2],"$t1")
			loadvr(generalList[i][3],"$t2")
			final_code.write('sub,$t0,$t1,$t2\n')
			storerv("$t1",generalList[i][4])
		#MULTILICATION
		elif (generalList[i][1] == '*'): 
			loadvr(generalList[i][2],"$t1")
			loadvr(generalList[i][3],"$t2")
			final_code.write('mul,$t0,$t1,$t2\n')
			storerv("$t1",generalList[i][4])
		#DIVISION
		elif (generalList[i][1] == '/'): 
			loadvr(generalList[i][2],"$t1")
			loadvr(generalList[i][3],"$t2")
			final_code.write('div,$t0,$t1,$t2\n')
			storerv("$t1",generalList[i][4])
		#OUT
		elif (generalList[i][1] == 'out'): 
			final_code.write('li $v0,1\n')
			loadvr(generalList[i][2],"$a0")   
			final_code.write('syscall\n')
		#IN
		elif (generalList[i][1] == 'in'): 
			final_code.write('li $v0,5\n')
			final_code.write('syscall\n')
			storerv("$v0",generalList[i][2])   
		#RETURN
		elif (generalList[i][1] == 'retv'): 
			loadvr(generalList[i][2],"$t1")
			final_code.write('lw $t0,-8($sp)\n')
			final_code.write('sw $t1,($t0)\n')
		#BEGIN BLOCK
		elif (generalList[i][1] == "begin_block"):
			#we search for the entity inside the symbol code
			(sc,en)=search(generalList[i][2])
			#if our search is did not find the entity that means is the first scope aka main
			if sc!=0:
				final_code.write("sw $ra,($sp)\n")
			if sc==0:
				final_code.seek(0,os.SEEK_SET)
				final_code.write("j L"+str(generalList[i][0])+"\n")
				final_code.seek(0,os.SEEK_END)
				final_code.write("addi $sp,$sp,"+str(compute_offset())+"\n")
				final_code.write("move $s0,$sp\n")
		#NOT MAIN END BLOCK
		elif (generalList[i][1]== "end_block" and generalList[(i-1)][1]!="halt"):
			final_code.write("lw $ra,($sp)\njr $ra\n")
		#HALT FOR THE MAIN END BLOCK
		elif (generalList[i][1]== "halt"):
			final_code.write("syscall\n")
		#CALL 
		elif (generalList[i][1]== "call" ):
			#when we find the call we must reset the counter for the parameters in order to get the correct order of them
			parCounter=0
			(sc,en)=search(generalList[i][2])
			#if the caller and the callee have the same scope level 
			if sc.scope_lvl==current_scope.scope_lvl:
				final_code.write("lw $t0,-4($sp)\nsw $t0,-4($fp)\n")
			#if the caller and the callee have different scope level 
			elif sc.scope_lvl!=current_scope.scope_lvl:
				final_code.write("sw $sp,-4($fp)\n")
			for i in range(len(resultList)):
				if(resultList[i][1]=="begin_block" and resultList[i][2]==en.name):#getting the startQuad of the subprogram
					en.subprogram.startQuad=resultList[i][0]+1
			final_code.write("addi $sp,$sp,"+str(en.subprogram.frameLength)+"\n jal L"+str(en.subprogram.startQuad)+"\naddi $sp,$sp,-"+str(en.subprogram.frameLength)+"\n")
		#PAR
		elif(generalList[i][1]=="par"):
			(sc,en)=search(generalList[i][2])
			#if this is the first parameter we come across
			if parCounter==0:
				final_code.write("addi $fp,$sp,"+str(sc.entityList[-1].subprogram.frameLength)+"\n")
			parCounter+=1
			#if its not the first parameter and is passed with value
			if (generalList[i][3]=="CV"):
				loadvr(generalList[i][2],"$t0")
				final_code.write("sw $t0,-"+str(12+4*parCounter)+"($fp)\n")
			#if its not the first parameter and is passed with reference
			elif (generalList[i][3]=="REF"):
				(sc,en)=search(generalList[i][2])
				#if the caller and the callee have the same scope level 
				if (sc.scope_lvl==current_scope.scope_lvl):
					#if its a variable or a parameter with value
					if (en.type=="VAR") or(en.type=="PARAM" and en.parameter.par_mode=="cv"):
						final_code.write("add $t0,$sp,-"+str(en.var.offset)+"\n")
						final_code.write("sw $t0,-"+str(12+4*parCounter)+"($fp)\n")
					#if its a parameter with reference
					elif(en.type=="PARAM" and en.parameter.par_mode=="REF"):
						final_code.write("lw $t0,-"+str(en.parameter.offset)+"($sp)\n")
				#if the caller and the callee have  different scope level 
				elif (sc.scope_lvl!=current_scope.scope_lvl):
					#if its a variable or a parameter with value
					if (en.type=="VAR") or(en.type=="PARAM" and en.parameter.par_mode=="cv"):
						gnlvcode(generalList[i][2])
						final_code.write("sw $t0,-"+str(12+4*parCounter)+"($fp)\n")
					#if its a parameter with reference			
					elif (en.type=="PARAM" and en.parameter.par_mode=="REF"):
						gnlvcode(generalList[i][2])
						final_code.write("lw $t0,($t0)\nsw $t0,-"+str(12+4*parCounter)+"($fp)\n")
			#if a parameter returns a value
			elif (generalList[i][3]=="RET"):
				final_code.write("addi $t0,$sp,-"+str(en.parameter.offset)+"\nsw $t0,-8($fp)\n")
		final_code.write("\n")
	#here we are clearing the generalList to avoid printing duplicate 
	generalList=[]

#here we go through the result list to check if there is a return in a procedure or there is a function without a return in order to use check_for_returns we created two new lists one for procedures and one for functions
def check_for_returns():
	for j in range(len(procedureList)):
		for i in range(len(resultList)):
			if resultList[i][1]=="begin_block" and resultList[i][2]==procedureList[j]:
				return_couter=1
			if resultList[i][1]=="retv":
				return_couter=0
			if resultList[i][1]== "end_block" and resultList[i][2]==procedureList[j]:
				break
		if return_couter==0:
			print("Error there should not be a return in any procedure!!\nA return exist inside "+procedureList[j])
			exit(-1)
	for j in range(len(functionList)):
		for i in range(len(resultList)):
			if resultList[i][1]=="begin_block" and resultList[i][2]==functionList[j]:
				return_couter=1
			if resultList[i][1]=="retv":
				return_couter=0
			if resultList[i][1]== "end_block" and resultList[i][2]==functionList[j]:
				break
		if return_couter==1:
			print("Error a function should always have a return!!\n"+functionList[j]+ " has no return")
			exit(-1)
functionList=[]
procedureList=[]	
def Syntax_analyzer():
    global getlines
    global Word_analyzer
    Word_analyzer=lex()
    getlines = Word_analyzer[3]
    def Program():
        global getlines
        global Word_analyzer
        global status
        if(Word_analyzer[0] ==DictOfStrTokens.get(124)):
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
            if(Word_analyzer[0] == DictOfStrTokens.get(100)):
                name=Word_analyzer[2]
                Word_analyzer = lex()
                getlines = Word_analyzer[3]
                statusFlag=1
                Blocks(name,statusFlag)
                if(Word_analyzer[0] == DictOfStrTokens.get(123)):
                    Word_analyzer = lex()
                    getlines = Word_analyzer[3]
                    return
                else:
                    print('Syntax error :\n "." expected to finish your program on line : ', getlines)
                    exit(1)
            else:
                print('Syntax error :\n An id for the program is expected on line: ', getlines)
                exit(1)
        else:
            print('Syntax error :\n The word "program" is expected on the beginning on line :  ', getlines)
            exit(1)

    def Blocks(name,statusFlag):
        global status
        global current_scope
        global counter_begin
        counter_begin=0
        add_scope(name)
        if (statusFlag==0):
        	pass_parameters()
        Declarations()
        Subprograms()
        genQuad('begin_block',name,'_','_')
        counter_begin+=1
        if (statusFlag==0):
        		# if the block(procedure/function) is not the main block calculate the Quad the block begins
        		current_scope.parent_scope.entityList[-1].subprogram.startQuad=nextQuad() 
        Statements()
        if (statusFlag==1):
            genQuad('halt','_','_','_')
        else:
        	# also before the end_block if its not the main block calculate the framelength (the offset of the last entity on the parent scope of our current one) 
        	current_scope.parent_scope.entityList[-1].subprogram.frameLength=compute_offset()
        genQuad('end_block',name,'_','_')
        if (len(scope_list)!=1):
        	print_Symbols()
        final()
        #closing all scopes except the main one 
        if (len(scope_list)!=1):
        	close_scope()
    def Declarations():
        global Word_analyzer
        global tempListDec
        while(Word_analyzer[0] ==DictOfStrTokens.get(125)):
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
            VarList()
            if(Word_analyzer[0] ==DictOfStrTokens.get(113)):
                Word_analyzer = lex()
                getlines = Word_analyzer[3]
            else:
                print('Syntax error :\n ";" was expected on line : ', getlines)
                exit(1)
        return

    def VarList():
        global Word_analyzer
        global tempListDec
        if(Word_analyzer[0] == DictOfStrTokens.get(100)):
        	#creating an entity for all the variables for a subprogram (we do the same inside the while line 734) all the variables are INT so we dont have var type
            newEntity=Entity()
            newEntity.type="VAR"
            newEntity.name=Word_analyzer[2]
            newEntity.var.offset=compute_offset()
            add_entities(newEntity)
            tempListDec+=[Word_analyzer[2]]
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
            while(Word_analyzer[0] == DictOfStrTokens.get(112)):
                Word_analyzer = lex()
                newEntity=Entity()
                newEntity.type="VAR"
                newEntity.name=Word_analyzer[2]
                newEntity.var.offset=compute_offset()
                add_entities(newEntity)
                getlines = Word_analyzer[3]
                if(Word_analyzer[0] == DictOfStrTokens.get(100)):
                    tempListDec+=[Word_analyzer[2]]
                    Word_analyzer = lex()
                    getlines = Word_analyzer[3]
                else:
                    print('Syntax error :\n varlist should be in the form of ID,ID,ID,..', getlines)
                    exit(1)
        return

    def Subprograms():
        global Word_analyzer
        while((Word_analyzer[0] == DictOfStrTokens.get(135)) or (Word_analyzer[0] == DictOfStrTokens.get(134))):
            Subprogram()

    def Subprogram():
        global Word_analyzer
        global procedureList
        global functionList
        if(Word_analyzer[0]==DictOfStrTokens.get(135)):
            Word_analyzer=lex()
            getlines=Word_analyzer[3]
            if(Word_analyzer[0]==DictOfStrTokens.get(100)):
                name=Word_analyzer[2]
                #creating an entity for the function 
                newEntity=Entity()
                newEntity.type="SUBPR"
                newEntity.name=name
                newEntity.subprogram.type="Function"
                newEntity.subprogram.startQuad=nextQuad()
                newEntity.subprogram.frameLength=compute_offset()
                add_entities(newEntity)
                #adding the function to functionList to be used later
               	functionList.append(name)
                Word_analyzer = lex()
                getlines = Word_analyzer[3]
                if(Word_analyzer[0] == DictOfStrTokens.get(114)):
                    Word_analyzer = lex()
                    getlines = Word_analyzer[3]
                    FormalparList()
                    if(Word_analyzer[0] == DictOfStrTokens.get(115)):
                        Word_analyzer = lex()
                        getlines = Word_analyzer[3]
                        statusFlag=0
                        Blocks(name,0)
                        return
                    else:
                        print('Syntax error :\n ")" expected on line :',getlines)
                        exit(1)
                else:
                    print('Syntax error :\n "(" expected on line : ',getlines)
                    exit(1)
            else:
                print('Syntax error :\n An acceptable Id is expected after "function" on line : ', getlines)
                exit(1)
        elif(Word_analyzer[0] == DictOfStrTokens.get(134)):
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
            if (Word_analyzer[0] == DictOfStrTokens.get(100)):
                name=Word_analyzer[2]
                #creating an entity for the Procedure                 
                newEntity=Entity()
                newEntity.type="SUBPR"
                newEntity.name=name
                newEntity.subprogram.type="Procedure"
                add_entities(newEntity)
                #adding the  procedure to procedureList to be used later                
                procedureList.append(name)
                Word_analyzer = lex()
                getlines = Word_analyzer[3]
                if (Word_analyzer[0] == DictOfStrTokens.get(114)):
                    Word_analyzer = lex()
                    getlines = Word_analyzer[3]
                    FormalparList()
                    if (Word_analyzer[0] == DictOfStrTokens.get(115)):
                        Word_analyzer = lex()
                        getlines = Word_analyzer[3]
                        Blocks(name,0)
                        return
                    else:
                        print('Syntax error :\n ")" expected on line :', getlines)
                        exit(1)
                else:
                    print('Syntax error :\n "(" expected on line : ', getlines)
                    exit(1)
            else:
                print('Syntax error :\n An acceptable Id is expected after "procedure" on line : ', getlines)
                exit(-1)

    def FormalparList():
        global Word_analyzer
        FormalparItem()
        while(Word_analyzer[0] == DictOfStrTokens.get(112)):
            Word_analyzer  = lex()
            getlines = Word_analyzer[3]
            FormalparItem()
        return

    def FormalparItem():
        global Word_analyzer
        global getlines
        if(Word_analyzer[0] == DictOfStrTokens.get(138)):
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
            if(Word_analyzer[0]== DictOfStrTokens.get(100)):
            	#creating an entity for each argument and if its in the parMode will be CV
                newArgument=Argument()
                newArgument.name=Word_analyzer[2]
                newArgument.parMode="CV"
                add_arguments(newArgument)
                Word_analyzer = lex()
                getlines = Word_analyzer[3]
            else:
                print('Syntax error :\n An id  is expected after the In Operator on line : ', getlines)
                exit(1)
        elif(Word_analyzer[0] == DictOfStrTokens.get(139)):
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
            if(Word_analyzer[0] == DictOfStrTokens.get(100)):
            	#creating an entity for each argument and if its inout the parMode will be REF
               	newArgument=Argument()
               	newArgument.name=Word_analyzer[2]
               	newArgument.parMode="REF"
               	add_arguments(newArgument)
               	Word_analyzer = lex()
                getlines = Word_analyzer[3]
            else:
                print('Syntax error :\n An id  is expected after the Inout Operator on line : ', getlines)
                exit(1) 
        elif ((Word_analyzer[0]!=DictOfStrTokens.get(138) and Word_analyzer[0]==DictOfStrTokens.get(100)) or (Word_analyzer[0]!=DictOfStrTokens.get(139) and Word_analyzer[0]==DictOfStrTokens.get(100))):
            print('Syntax error :\n Par list should be in the form of (in/inout var , in/inout var ,...) on line :',getlines)
            exit(1)
        return

    def Statements():
        global Word_analyzer
        global getlines
        if(Word_analyzer[0] == DictOfStrTokens.get(118)):
            Word_analyzer = lex()
            getlines=Word_analyzer[3]
            Statement()
            while(Word_analyzer[0] ==DictOfStrTokens.get(113)):
                Word_analyzer = lex()
                getlines = Word_analyzer[3]
                Statement()
            if(Word_analyzer[0]==DictOfStrTokens.get(119)):
                Word_analyzer=lex()
                getlines=Word_analyzer[3]
                return
            else:
                    print('Syntax error :\n i) The Statements must be in the form of { statement ( ; statement )∗} or \n ii) "}" is expected to close the statements on line : ', getlines)
                    exit(1)
        else:
            Statement()
            if(Word_analyzer[0] == DictOfStrTokens.get(113)):
                Word_analyzer = lex()
                getlines = Word_analyzer[3]
                return
            else:
                print('Syntax error :\n ";" is expected on line : ', getlines)
                exit(1)

    def Statement():
        global Word_analyzer
        if(Word_analyzer[0]==DictOfStrTokens.get(100)):
            Assignment_Stat()
        elif(Word_analyzer[0] == DictOfStrTokens.get(126)):
            If_Stat()
        elif(Word_analyzer[0] == DictOfStrTokens.get(128)):
            While_Stat()
        elif (Word_analyzer[1] == 136):
            Call_Stat()
        elif (Word_analyzer[0] == DictOfStrTokens.get(137)):
            Return_Stat()
        elif (Word_analyzer[0] == DictOfStrTokens.get(143)):
            Input_Stat()
        elif (Word_analyzer[0] == DictOfStrTokens.get(144)):
            Print_Stat()
        elif(Word_analyzer[0] == DictOfStrTokens.get(129)):
            Switchcase_Stat()
        elif(Word_analyzer[0] == DictOfStrTokens.get(131)):
            Forcase_Stat()
        elif(Word_analyzer[0] == DictOfStrTokens.get(130)):
            Incase_Stat()
        return

    def Assignment_Stat():
        global Word_analyzer
        if (Word_analyzer[0] == DictOfStrTokens.get(100)):
            assignmentId=Word_analyzer[2]
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
            if (Word_analyzer[0] == DictOfStrTokens.get(122)):
                Word_analyzer = lex()
                getlines = Word_analyzer[3]
                E_Place=Expression()
                genQuad(':=',E_Place,'_',assignmentId)
                return
            else:
                print('Syntax error :\n ":=" is expected to assign an expression on line : ', getlines)
                exit(1)
        else:
            print('Syntax error :\n An ID is expected so an expression is assigned to , on line : ', getlines,'on ',Word_analyzer[0])
            exit(1)

    def If_Stat():
        global Word_analyzer
        global getlines
        Word_analyzer= lex()
        getlines = Word_analyzer[3]
        if(Word_analyzer[0] == DictOfStrTokens.get(114)):
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
            ConditionList=Condition()
            backPatch(ConditionList[0],nextQuad())
            if(Word_analyzer[0]== DictOfStrTokens.get(115)):
                Word_analyzer = lex()
                getlines = Word_analyzer[3]
                Statements()
                ifList=makeList(nextQuad())
                genQuad('jump','_','_','_')
                backPatch(ConditionList[1],nextQuad())
                ElsePart()
                backPatch(ifList,nextQuad())
            else:
                print('Syntax error :\n ")" expected after if condition ends on line :', getlines)
                exit(1)
        else:
            print('Syntax error :\n "(" expected before if condition begins on line :', getlines)
            exit(1)
        return 

    def ElsePart():
        global Word_analyzer
        global getlines
        if(Word_analyzer[0] == DictOfStrTokens.get(127)):
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
            Statements()
            return

    def While_Stat():
        global Word_analyzer
        global getlines
        Word_analyzer = lex()
        getlines = Word_analyzer[3]
        if(Word_analyzer[0] == DictOfStrTokens.get(114)):
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
            quadCounter=nextQuad()
            ConditionList=Condition()
            backPatch(ConditionList[0],nextQuad())
            if(Word_analyzer[0] == DictOfStrTokens.get(115)):
                Word_analyzer = lex()
                getlines = Word_analyzer[3]
                Statements()
                genQuad('jump','_','_',quadCounter)
                backPatch(ConditionList[1],nextQuad())
            else:
                print('Syntax error :\n ")" expected after while condition ends on line :', getlines)
                exit(1)
        else:
            print('Syntax error :\n "(" expected before while condition begins on line :', getlines)
            exit(1)
        

    def Switchcase_Stat():
        global Word_analyzer
        global getlines
        Word_analyzer = lex()
        getlines = Word_analyzer[3]
        outList=emptyList()
        while(Word_analyzer[0] == DictOfStrTokens.get(132)):
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
            if(Word_analyzer[0] == DictOfStrTokens.get(114)):
                Word_analyzer = lex()
                getlines = Word_analyzer[3]
                ConditionList=Condition()
                backPatch(ConditionList[0],nextQuad())
                if(Word_analyzer[0] == DictOfStrTokens.get(115)):
                    Word_analyzer = lex()
                    getlines = Word_analyzer[3]
                    Statements()
                    outJump = makeList(nextQuad())
                    genQuad('jump','_','_','_')
                    outList=merge(outList,outJump)
                    backPatch(ConditionList[1],nextQuad())
                    
                else:
                    print('Syntax error :\n ")" expected after Switch case condition ends on line :', getlines)
                    exit(1)
            else:
                print('Syntax error :\n "(" expected after Switch case condition begins on line :', getlines)
                exit(1)
        if(Word_analyzer[0] == DictOfStrTokens.get(133)):
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
            Statements()
            backPatch(outList,nextQuad())
        else:
            print('Syntax error :\n "default" expected before the default statements on line :', getlines)
            exit(1)

    def Forcase_Stat():
        global Word_analyzer
        global getlines
        Word_analyzer = lex()
        getlines = Word_analyzer[3]
        StartOfForcase=nextQuad()
        while(Word_analyzer[0] == DictOfStrTokens.get(132)):
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
            if(Word_analyzer[0] == DictOfStrTokens.get(114)):
                Word_analyzer = lex()
                getlines = Word_analyzer[3]
                ConditionList=Condition()
                backPatch(ConditionList[0],nextQuad())
                if(Word_analyzer[0] == DictOfStrTokens.get(115)):
                    Word_analyzer = lex()
                    getlines = Word_analyzer[3]
                    Statements()
                    genQuad('jump','_','_',StartOfForcase)
                    backPatch(ConditionList[1],nextQuad())
                else:
                    print('Syntax error :\n ")" expected after case condition ends on line :', getlines)
                    exit(1)
            else:
                print('Syntax error :\n "(" expected after case condition begins on line :', getlines)
                exit(1)
        if(Word_analyzer[0] == DictOfStrTokens.get(133)):
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
            Statements()
        else:
            print('Syntax error :\n "default" expected before the default statements on line :', getlines)
            exit(1)

    def Incase_Stat():
        global Word_analyzer
        global getlines
        Word_analyzer = lex()
        getlines = Word_analyzer[3]
        P1_Quad=nextQuad()
        w=newTemp()
        genQuad(':=','1','_',w)
        while(Word_analyzer[0] == DictOfStrTokens.get(132)):
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
            if(Word_analyzer[0] == DictOfStrTokens.get(114)):
                Word_analyzer = lex()
                getlines = Word_analyzer[3]
                ConditionList=Condition()
                backPatch(ConditionList[0],nextQuad())
                if(Word_analyzer[0] == DictOfStrTokens.get(115)):
                    Word_analyzer = lex()
                    getlines = Word_analyzer[3]
                    Statements()
                    genQuad(':=','0','_',w)
                    backPatch(ConditionList[1],nextQuad())
                else:
                    print('Syntax error :\n ")" expected before the case conditions on line :', getlines)
                    exit(1)
            else:
                print('Syntax error :\n ")" expected before the case conditions on line :', getlines)
                exit(1)
        genQuad('=',w,'0',P1_Quad)

    def Return_Stat():
        global Word_analyzer
        global getlines
        Word_analyzer = lex()
        getlines = Word_analyzer[3]
        if(Word_analyzer[0] == DictOfStrTokens.get(114)):
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
            E_Place=Expression()
            if(Word_analyzer[0] == DictOfStrTokens.get(115)):
                Word_analyzer = lex()
                getlines = Word_analyzer[3]
                genQuad('retv',E_Place,'_','_')
            else:
                print('Syntax error :\n ")" is expected after the expression of the return stat on line :', getlines)
                exit(1)
        else:
            print('Syntax error :\n "(" is expected before the expression of the return stat on line :', getlines)
            exit(1)
        return

    def Call_Stat():
        global Word_analyzer
        global getlines
        Word_analyzer=lex()
        if(Word_analyzer[0] == DictOfStrTokens.get(100)):
            name=Word_analyzer[2]
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
            if(Word_analyzer[0] == DictOfStrTokens.get(114)):
                Word_analyzer = lex()
                getlines = Word_analyzer[3]
                ActualparList()
                genQuad('call',name,'_','_')
                if(Word_analyzer[0] == DictOfStrTokens.get(115)):
                    Word_analyzer = lex()
                    getlines = Word_analyzer[3]
                    return
                else:
                    print('Syntax error :\n ")" is expected after call ActualParList on line :', getlines)
                    exit(1)
            else:
                print('Syntax error :\n "(" is expected before call ActualParList on line :', getlines)
                exit(1)
        else:
            print('Syntax error:\n Not acceptable Id has been given to Call State', getlines)
            exit(1)

    def Print_Stat():
        global Word_analyzer
        global getlines
        Word_analyzer = lex()
        getlines = Word_analyzer[3]
        if(Word_analyzer[0] == DictOfStrTokens.get(114)):
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
            E_Place=Expression()
            if(Word_analyzer[0] == DictOfStrTokens.get(115)):
                Word_analyzer = lex()
                getlines = Word_analyzer[3]
                genQuad('out',E_Place,'_','_')
            else:
                print('Syntax error :\n ")" is expected after the expression of the print stat on line :', getlines)
                exit(1)
        else:
            print('Syntax error :\n "(" is expected before the expression of the print stat on line :', getlines)
            exit(1)
        return

    def Input_Stat():
        global Word_analyzer
        global getlines
        Word_analyzer = lex()
        getlines = Word_analyzer[3]
        if(Word_analyzer[0] == DictOfStrTokens.get(114)):
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
            if(Word_analyzer[0] == DictOfStrTokens.get(100)):
                Id_Place=Word_analyzer[2]
                Word_analyzer = lex()
                getlines = Word_analyzer[3]
                genQuad('inp',Id_Place,'_','_')
                if(Word_analyzer[0] == DictOfStrTokens.get(115)):
                    Word_analyzer = lex()
                    getlines = Word_analyzer[3]
                    return
                else:
                    print('Syntax error :\n ")" is expected after the Id of the Input stat on line :', getlines)
                    exit(1)
            else:
                print('Syntax error :\n An Id is expected to get the Input stat on line :', getlines)
                exit(1)
        else:
            print('Syntax error :\n "(" is expected before the Id of the Input stat on line :', getlines)
            exit(1)

    def ActualparList():
        global Word_analyzer
        global getlines
        ActualparItem()
        while(Word_analyzer[0] == DictOfStrTokens.get(112)):
            Word_analyzer  = lex()
            getlines = Word_analyzer[3]
            ActualparItem()

    def ActualparItem():
        global Word_analyzer
        global getlines
        if(Word_analyzer[0] == DictOfStrTokens.get(138)):
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
            this_Expression=Expression()
            genQuad('par',this_Expression,'CV','_')
        elif(Word_analyzer[0] == DictOfStrTokens.get(139)):
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
            if(Word_analyzer[0] == DictOfStrTokens.get(100)):
                this_name=Word_analyzer[2]
                Word_analyzer = lex()
                getlines = Word_analyzer[3]
                genQuad('par',this_name,'REF','_')
            else:
                print('Syntax error :\n An Id is expected for the InOut operator', getlines)
                exit(1)
        elif ((Word_analyzer[0]!=DictOfStrTokens.get(138) and Word_analyzer[0]==DictOfStrTokens.get(100)) or (Word_analyzer[0]!=DictOfStrTokens.get(139)and Word_analyzer[0]==DictOfStrTokens.get(100))):
            print('Syntax error :\n Par list should be in the form of (in/inout var , in/inout var ,...) on line : ',getlines)
            exit(1)
        return

    def Condition():
        global Word_analyzer
        global getlines
        ConditionTrue = []
        ConditionFalse = []
        Bool_Term1 = BoolTerm()
        ConditionTrue = Bool_Term1[0]
        ConditionFalse = Bool_Term1[1]
        while (Word_analyzer[0] == DictOfStrTokens.get(141)):
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
            backPatch(ConditionFalse,nextQuad())
            Bool_Term2=BoolTerm()
            ConditionTrue=merge(ConditionTrue,Bool_Term2[0])
            ConditionFalse=Bool_Term2[1]
        return ConditionTrue,ConditionFalse

    def BoolTerm():
        global Word_analyzer
        global getlines
        BoolTermTrue=[]
        BoolTermFalse=[]
        Bool_Factor1=BoolFactor()
        BoolTermTrue=Bool_Factor1[0]
        BoolTermFalse=Bool_Factor1[1]
        while (Word_analyzer[0] == DictOfStrTokens.get(140)):#AND
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
            backPatch(BoolTermTrue,nextQuad())
            Bool_Factor2=BoolFactor()
            BoolTermFalse=merge(BoolTermFalse,Bool_Factor2[1])
            BoolTermTrue=Bool_Factor2[0]
        return BoolTermTrue,BoolTermFalse

    def BoolFactor():
        global Word_analyzer
        global getlines
        BoolFactor_True=[]
        BoolFactor_False=[]
        if (Word_analyzer[0] == DictOfStrTokens.get(142)):
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
            if (Word_analyzer[0] == DictOfStrTokens.get(116)):
                Word_analyzer = lex()
                getlines = Word_analyzer[3]
                ConditionList=Condition()
                if (Word_analyzer[0] == DictOfStrTokens.get(117)):
                    Word_analyzer = lex()
                    getlines = Word_analyzer[3]
                    BoolFactor_True=ConditionList[1]
                    BoolFactor_False=ConditionList[0]
                else:
                    print('Syntax error :\n "]" expected after conditions ends in BoolFactor', getlines)
                    exit(1)
            else:
                print('Syntax error :\n "[" expected after not in BoolFactor', getlines)
                exit(1)
        elif (Word_analyzer[0] == DictOfStrTokens.get(116)):
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
            ConditionList=Condition()
            if (Word_analyzer[0] == DictOfStrTokens.get(117)):
                Word_analyzer = lex()
                getlines = Word_analyzer[3]
                BoolFactor_True=ConditionList[0]
                BoolFactor_False=ConditionList[1]
            else:
                print('Syntax error :\n "]" expected after conditions ends in BoolFactor', getlines)
                exit(1)
        else:
            E_Place1=Expression()
            Rel_Operator=Relational_Oper()
            E_Place2=Expression()
            BoolFactor_True=makeList(nextQuad())
            genQuad(Rel_Operator,E_Place1,E_Place2,'_')
            BoolFactor_False=makeList(nextQuad())
            genQuad('jump','_','_','_')
        return BoolFactor_True,BoolFactor_False

    def Expression():
        global Word_analyzer
        global getlines
        op_sign=Optional_Sign()
        T1_place=op_sign+Term()
        while (Word_analyzer[0] == DictOfStrTokens.get(110) or Word_analyzer[0] == DictOfStrTokens.get(111)):
            addop=Word_analyzer[2]
            Add_Oper()
            T2_place=Term()
            w=newTemp()
            genQuad(addop,T1_place,T2_place,w)
            T1_place=w
        E_Place=T1_place
        return E_Place

    def Term():
        global Word_analyzer
        global getlines
        F1_place=Factor()
        while (Word_analyzer[0] == DictOfStrTokens.get(108) or Word_analyzer[0] == DictOfStrTokens.get(109)):
            mulOperator=Word_analyzer[2]
            Mul_Oper()
            F2_place=Factor()
            w=newTemp()
            genQuad(mulOperator,F1_place,F2_place,w)
            F1_place=w
        tplace=F1_place    
        return tplace

    def Factor():
        global Word_analyzer
        global getlines
        returnable=''
        if (Word_analyzer[0] == DictOfStrTokens.get(101)):
            factorPassdown=Word_analyzer[2]
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
        elif (Word_analyzer[0] == DictOfStrTokens.get(114)):
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
            E_Place=Expression()
            if (Word_analyzer[0] == DictOfStrTokens.get(115)):
                factorPassdown=E_Place
                Word_analyzer = lex()
                getlines = Word_analyzer[3]
            else:
                print('Syntax error :\n ")" expected after expression in Factor', getlines)
                exit(1)
        elif (Word_analyzer[0] == DictOfStrTokens.get(100)):
            factorPassdown=Word_analyzer[2]
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
            returnable=IdTail(factorPassdown)
        else:
            print('Syntax error:\n expected constant or expression or Id in Factor after the ',Word_analyzer[0], 'on line : ' , getlines)
            exit(1)
        if (returnable==''):
            return factorPassdown
        return returnable

    def IdTail(name):
        global Word_analyzer
        global getlines
        w=''
        if (Word_analyzer[0] == DictOfStrTokens.get(114)):
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
            ActualparList()
            w=newTemp()
            genQuad('par',w,'RET','_')
            genQuad('call',name,'_','_')
            if (Word_analyzer[0] == DictOfStrTokens.get(115)):
                Word_analyzer = lex()
                getlines = Word_analyzer[3]
        return w

    def Optional_Sign():
        global Word_analyzer
        global getlines
        operator=''
        if (Word_analyzer[0] == DictOfStrTokens.get(110) or Word_analyzer[0] == DictOfStrTokens.get(111)):
            if (Word_analyzer[0]==DictOfStrTokens.get(111)):
                operator=Word_analyzer[2]
            Add_Oper()
        return operator

    def Relational_Oper():
        global Word_analyzer
        global getlines
        if (Word_analyzer[0] == DictOfStrTokens.get(104)):
            Rel_Operator=Word_analyzer[2]
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
        elif (Word_analyzer[0] == DictOfStrTokens.get(102)):
            Rel_Operator=Word_analyzer[2]
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
        elif (Word_analyzer[0] == DictOfStrTokens.get(105)):
            Rel_Operator=Word_analyzer[2]
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
        elif (Word_analyzer[0] == DictOfStrTokens.get(107)):
            Rel_Operator=Word_analyzer[2]
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
        elif (Word_analyzer[0] == DictOfStrTokens.get(103)):
            Rel_Operator=Word_analyzer[2]
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
        elif (Word_analyzer[0] == DictOfStrTokens.get(106)):
            Rel_Operator=Word_analyzer[2]
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
        else:
            print('Syntax error: \nthe relational operator must be one of the following (1)"<>",(2)"<",(3)">",(4)"<=",(5)">=",(6)"="  on line :' , getlines)
            exit(1)
        return Rel_Operator

    def Add_Oper():
        global Word_analyzer
        global getlines
        sub_op=''
        if (Word_analyzer[0] == DictOfStrTokens.get(110)):
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
        elif (Word_analyzer[0] == DictOfStrTokens.get(111)):
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
            sub_op = Word_analyzer[2]
        return sub_op
        
    def Mul_Oper():
        global Word_analyzer
        global getlines
        if (Word_analyzer[0] == DictOfStrTokens.get(108)):
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
        elif (Word_analyzer[0] == DictOfStrTokens.get(109)):
            Word_analyzer = lex()
            getlines = Word_analyzer[3]
        return
    Program()
Syntax_analyzer()
check_for_returns()
def IntFile():
    global resultList
    Fname=sys.argv[1]
    Fname=Fname.replace(".ci","")
    Fname+=".int"
    intfile=open(Fname,"w")
    for i in range(len(resultList)):
    	intfile.write("["+str(resultList[i][0])+" : "+str(resultList[i][1])+" , "+str(resultList[i][2])+" , "+str(resultList[i][3])+" , "+str(resultList[i][4])+"]\n")
    intfile.close()
def Equal_to_C():
    global tableOfTemps
    global tempListDec
    Fname=sys.argv[1]
    Fname=Fname.replace(".ci","")
    Fname+=".c"
    c_Text = open(Fname,'w')
    c_Text.write("int main ( ){\n\t")
    tableOfTemps+=tempListDec
    if(len(tableOfTemps)!=0):
    	c_Text.write("int ")
    for i in range(len(tableOfTemps)):
    	c_Text.write(tableOfTemps[i])
    	if(len(tableOfTemps) == i+1):
    		c_Text.write(" ;\n\t")
    	else:
    		c_Text.write(",")	
    for j in range(len(resultList)):
    	nextj=j+1
    	jumpNum=str(resultList[j][4])
    	if(resultList[j][1] == 'begin_block'):
    		c_Text.write("L_"+str(nextj)+" : \n\t")
    	elif(resultList[j][1] == ":="):
    		c_Text.write("L_"+str(nextj)+" : "+ resultList[j][4]+" = "+resultList[j][2]+" ;\n\t")
    	elif(resultList[j][1] == "+"):
    		c_Text.write("L_"+str(nextj)+" : "+ resultList[j][4]+" = "+resultList[j][2]+" + "+resultList[j][3]+" ;\n\t")
    	elif(resultList[j][1] == "-"):
    		c_Text.write("L_"+str(nextj)+" : "+ resultList[j][4]+" = "+resultList[j][2]+" - "+resultList[j][3]+" ;\n\t")
    	elif(resultList[j][1] == "*"):
    		c_Text.write("L_"+str(nextj)+" : "+ resultList[j][4]+" = "+resultList[j][2]+" * "+resultList[j][3]+" ;\n\t")
    	elif(resultList[j][1] == "/"):
    		c_Text.write("L_"+str(nextj)+" : "+ resultList[j][4]+" = "+resultList[j][2]+" / "+resultList[j][3]+" ;\n\t")
    	elif(resultList[j][1] == "jump"):
    		c_Text.write("L_"+str(nextj)+" : "+"goto L_"+str(resultList[j][4]-100)+ " ;\n\t")
    	elif(resultList[j][1] == "<"):
    		c_Text.write("L_"+str(nextj)+" : "+"if ("+resultList[j][2]+" < "+resultList[j][3]+") goto L_"+str(resultList[j][4]-100)+" ;\n\t")
    	elif(resultList[j][1] == ">"):
    		c_Text.write("L_"+str(nextj)+" : "+"if ("+resultList[j][2]+" > "+resultList[j][3]+") goto L_"+str(resultList[j][4]-100)+" ;\n\t")
    	elif(resultList[j][1] == ">="):
    		c_Text.write("L_"+str(nextj)+" : "+"if ("+resultList[j][2]+" >= "+resultList[j][3]+") goto L_"+str(resultList[j][4]-100)+" ;\n\t")
    	elif(resultList[j][1] == "<="):
    		c_Text.write("L_"+str(nextj)+" : "+"if ("+resultList[j][2]+" <= "+resultList[j][3]+") goto L_"+str(resultList[j][4]-100)+" ;\n\t")
    	elif(resultList[j][1] == "<>"):
    		c_Text.write("L_"+str(nextj)+" : "+"if ("+str(resultList[j][2])+" != "+str(resultList[j][3])+") goto L_"+str(resultList[j][4]-100)+" ;\n\t")
    	elif(resultList[j][1] == "="):
    		c_Text.write("L_"+str(nextj)+" : "+"if ("+resultList[j][2]+" == "+resultList[j][3]+") goto L_"+str(resultList[j][4]-100)+" ;\n\t")
    	elif(resultList[j][1] == "out"):
    		c_Text.write("L_"+str(nextj)+" : "+"printf(\""+resultList[j][2]+" = %d\","+resultList[j][2]+") ;\n\t")
    	elif(resultList[j][1] == 'halt'):
    		c_Text.write("L_"+str(nextj)+" : ")
    c_Text.write('\n}')
    c_Text.close()

global counter_begin
IntFile()
print('Syntax analyzer finished succesfully !')
if (counter_begin==1): 
    Equal_to_C()
    print('An equal programm in C language has been created')
else :
	print('There are functions or procedures in the program so an equal program to C has not been created')
print_Symbols()
