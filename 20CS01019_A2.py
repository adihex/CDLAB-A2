import re

numberRegex = re.compile(r"^[0-9]+(\.[0-9]+)?(E[+-]?[0-9]+)?$")
idRegex = re.compile(r"^[A-Za-z][A-Za-z0-9]*$")

def categorizeTestCases(testCases):
    categorized_test_cases = []
    for testCase in testCases:
        if testCase in ("then", "if", "else"):
            categorized_test_cases.append(f"({testCase},{testCase.upper()})")
        elif testCase in ("<", ">", ">=", "<=", "=", "<>"):
            categorized_test_cases.append(f"(relop,{testCase})")
        elif numberRegex.match(testCase):
            categorized_test_cases.append(f"(number,{testCase})")
        elif idRegex.match(testCase):
            categorized_test_cases.append(f"(id,{testCase})")
        else:
            categorized_test_cases.append(f"(Unrecognized,{testCase})")
    return categorized_test_cases

def buildArray(inputString):
    outputArray = []
    tempString = ""
    i=0
    while(i < len(inputString)):
        char=inputString[i]
        if char in (" ", "\n", "\t", "<", ">", "="):
            if tempString.strip():
                outputArray.append(tempString.strip())
            if(char in ("<",">","=") and inputString[i+1] in (">","<","=")):
                outputArray.append(char + inputString[i + 1])
                i += 1
            tempString = ""
        else:
            tempString += char
        i+=1
    if tempString.strip():
        outputArray.append(tempString.strip())
    return outputArray

def readInputFromFile(filename):
    with open(filename, "r", encoding="utf8") as file:
        return file.read()
        # for line in sys.stdin:
            # line=line.rstrip()
            # print(f"Message from stdin:{line}")
            # break
            # return line

def writeOutputToFile(filename, output):
    with open(filename, "w", encoding="utf8") as file:
        file.write("\n".join(output))

def main():
    inputFilePath = "input.txt"
    outputFilePath = "output.txt"
    inputString = readInputFromFile(inputFilePath)
    testCases = buildArray(inputString)
    categorizedTestCases = categorizeTestCases(testCases)
    for x in categorizedTestCases:
        print(x)
    writeOutputToFile(outputFilePath, categorizedTestCases)

if __name__ == "__main__":
    main()
