import sys
import re
import math
#regex_sub substitutes a sequence of charaters in a string
def regex_sub(string,sub,regex):
    return re.sub(regex,sub,string)
#remove_power will remove the power symbol within a string if present
def remove_power(component):
    return regex_sub(component,"","\^[0-2]")  

#substitute_variable will remove ny algebraic varaibles from the string and replace with a integer if necessary
def substitute_variable(component):
    if re.search("[0-9]+",component)!= None:
        return regex_sub(component,"","[a-zA-Z]")
    else:
        return regex_sub(component,"1","[a-zA-Z]")

#finding_terms
def finding_terms(input):
    
    quadRegex = "[+-]?[0-9]*[a-zA-Z]\^2"
    singleRegex = "[+-]?[0-9]*[a-zA-Z](\^1)?"
    # Extracting the integer values from the quadratic equation
    quad = remove_power(re.search(quadRegex,input).group())
    input = regex_sub(input,"",quadRegex)
    single = re.search(singleRegex,input)
    if single != None:
        single = remove_power(single.group())
    else:
        single = "0"
    input = regex_sub(input,"",singleRegex)
    coeffient = remove_power(re.search("[+-]?[0-9]*",input).group())
    
    # If there is no coeffient then set it to 0
    if coeffient == "":
        coeffient = "0"
    # Removes alegebraic variables
    quadValue = substitute_variable(quad)
    singleValue = substitute_variable(single)
  
    return int(quadValue),int(singleValue),int(coeffient)
    
#gcd_calculator calcualtes the greatest common denomiator
def gcd_calculator(a,b):
    while b:
        temp = a
        a = b
        b = temp%b
    return abs(a)
#display_num converts integer to string with correct sign
def display_num(x):
    if x>1:
        return " + "+str(x)
    elif x==0:
        return ""
        
    else:
        return " - "+str(abs(x))
#get_solution returns the solutions numerator and denominator
def get_solution(solNumber,denominator):
    # Greatest common denominator for each solution value
    solGcd = gcd_calculator(solNumber,denominator)
    # Calculate the coeffients
    solNumber = int(-solNumber/solGcd)
    solDenominator = int(denominator/solGcd)
    return solNumber,solDenominator
    
def main():
   
    input = sys.argv[1]
    a,b,c = finding_terms(input)

    gcdTemp = gcd_calculator(a,b)
    gcd = gcd_calculator(gcdTemp,c)
    determinate = (b**2-4*a*c)
    sol1Number = -b+determinate**(1/2)
    sol2Number = -b-determinate**(1/2)
    denominator = 2.0*a
    
    # Checks they are integers and not floats 
    if not (sol1Number.is_integer() and sol2Number.is_integer()) or not denominator.is_integer():
        print("Clean factorization not available")
    else:

        sol1Number,sol1Denominator = get_solution(sol1Number,denominator)
        sol2Number,sol2Denominator = get_solution(sol2Number,denominator)

        outerValue = int(gcd*a/abs(a))
        if outerValue == 1:
            outerValue = ""
        else :
            outerValue = str(outerValue)
        print(outerValue+"("+str(sol1Denominator)+"X"+display_num(sol1Number)+")("+str(sol2Denominator)+"X"+display_num(sol2Number)+")")

        

if __name__ == "__main__":
    main()

