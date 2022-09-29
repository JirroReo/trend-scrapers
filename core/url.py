# ---------------------------------------------------------------------------------------------------------------------------------------------
# Code written and updated by 
# Johann Benjamin Vivas (TR-PH-INTRN as of August 12, 2022) since July 2, 2022.
# Modified by Jirro Dave Reoloso (TR-PH-INTRN as of September 8, 2022)
# ---------------------------------------------------------------------------------------------------------------------------------------------

import pyperclip

def getDomain(s):
    newstr = s
    newstrspl = newstr.split("/")
    return str(newstrspl[2]).strip()

def splitbyLinesandSpace(s):
    L = preSplitLines(s)
    split = (x for x in L.split(" ") if (x != '' and not x.isspace()))
    return split

def splitbyLines(s):
    split = (x for x in s.splitlines() if (x != '' and not x.isspace()))
    return split

def preSplitLines(s):
    L = ""
    for lin in splitbyLines(s):
        L += "\n" 
        L += lin
    return L

def clearScreen():
    # "Clears" the screen
    for i in range(0,41):
        print("\n")

def getCounterpart(s):
    output = []
    if("http" in s[:8]):
        output.append(getDomain(s))
        output.append(s)
        return output
    else:
        output.append(s.lower().strip())
        output.append("https://{0}/".format(s.lower().strip()))
        return output.replace('.', '[.]')

def splitbyLinesandTabs(s):
    L = preSplitLines(s)
    split = (x for x in L.split("\t") if (x != '' and not x.isspace()))
    return split

def openandRead(fpath):
    final_string = ""
    with open(fpath) as f:
        string = f.readlines()
        for line in string:
            final_string += str(line)
    #print(final_string)
    return final_string

def processLinks():
    get_counterparts = 1
    split_mode = 2 #1 space, 2 lines, 3 tabs
    input_file_path = "input.txt"

    string = openandRead(input_file_path)

    if (split_mode == 1):
        splstr = splitbyLinesandSpace(string)
    elif(split_mode == 2):
        splstr = splitbyLines(string)
    elif (split_mode == 3):
        splstr = splitbyLinesandTabs(string)

    finalstring = []

    for s in splstr: #either get domain or add http, if both true, defaults to add http
        if(get_counterparts == 1):
            finalstring.append(getCounterpart(s)[0])
            finalstring.append(getCounterpart(s)[1])
            #print(getCounterpart(s))
        else:
            finalstring.append(s.replace('.', '[.]'))
            #print(s)

    try:
        pyperclip.copy('\n'.join(finalstring)) #use python 2 or 3 (make sure to fix paths for this)
        print("Successfully copied result to clipboard!")
        return finalstring
    except:
        print("An exception occurred; could not copy to clipboard.")

if __name__ == '__main__':
    print(processLinks())
