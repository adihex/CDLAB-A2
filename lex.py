import sys

digitRegex=r"^[0-9]$"
digitsRegex=r"^[0-9]+$"
numberRegex=r"^[0-9](\.[0-9])?(E[+-]?[0-9]+)?$"
letterRegex=r"[A-Za-z]$"
idRegex=r"[A-Za-z]([A-za-z]|[0-9])*$"



def read_input_from_file():
    with open(sys.argv[1],'r',encoding="utf8") as file:
        return file.read()

def write_output_to_file(output):
    with open(sys.argv[2],'w',encoding="utf8") as file:
        file.write("\n".join(output))

if __name__ == "__main__":
    inp=read_input_from_file()
    write_output_to_file(output)
    pass
