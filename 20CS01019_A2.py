import re

digitRegex = re.compile(r"^[0-9]$")
digitsRegex = re.compile(r"^[0-9]+$")
numberRegex = re.compile(r"^[0-9]+(\.[0-9]+)?(E[+-]?[0-9]+)?$")
letterRegex = re.compile(r"^[A-Za-z]$")
idRegex = re.compile(r"^[A-Za-z][A-Za-z0-9]*$")

def categorizeTestCases(testCases):
    categorized_test_cases = []
    for testCase in testCases:
        if testCase in ("then", "if", "else"):
            categorized_test_cases.append(f"({testCase},{testCase.upper()})")
        elif testCase in ("<", ">", ">=", "<=", "=", "<>"):
            categorized_test_cases.append(f"(relop,{testCase})")
        elif digitRegex.match(testCase):
            categorized_test_cases.append(f"(digit,{testCase})")
        elif numberRegex.match(testCase):
            categorized_test_cases.append(f"(number,{testCase})")
        elif digitsRegex.match(testCase):
            categorized_test_cases.append(f"(digits,{testCase})")
        elif letterRegex.match(testCase):
            categorized_test_cases.append(f"(letter,{testCase})")
        elif idRegex.match(testCase):
            categorized_test_cases.append(f"(id,{testCase})")
        else:
            categorized_test_cases.append(f"(Unrecognized,{testCase})")
    return categorized_test_cases

def buildArray(inputString):
    outputArray = []
    tempString = ""
    i=0
    for char in inputString:
        if char in (" ", "\n", "\t", "<", ">", "="):
            if tempString.strip():
                outputArray.append(tempString.strip())
            if char in ("<", ">", "=") and inputString[i + 1] == char:
                outputArray.append(char + inputString[i + 1])
                i += 1
            elif char in ("<", ">", "="):
                outputArray.append(char)
            tempString = ""
        else:
            tempString += char
    if tempString.strip():
        outputArray.append(tempString.strip())
    return outputArray

def readInputFromFile(filename):
    with open(filename, "r", encoding="utf8") as file:
        return file.read()

def writeOutputToFile(filename, output):
    with open(filename, "w", encoding="utf8") as file:
        file.write("\n".join(output))

def main():
    inputFilePath = "input.txt"
    outputFilePath = "output.txt"

    inputString = readInputFromFile(inputFilePath)
    testCases = buildArray(inputString)
    categorizedTestCases = categorizeTestCases(testCases)

    writeOutputToFile(outputFilePath, categorizedTestCases)

if __name__ == "__main__":
    main()
