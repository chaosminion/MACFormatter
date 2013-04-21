'''
This script will convert a given MAC address to a colon delimited format.
Python 3.3
'''

from tkinter import *
from tkinter import ttk

class GUI(object):
    '''
    This class will run the GUI.
    '''

    def __init__(self, myParent):

        self.masterFrame = ttk.Frame(myParent)
        masterFrame = self.masterFrame
        masterFrame.grid(column=0, row=0)

        unformatedMACAddress = ''
        
        self.MACEntry = ttk.Entry(masterFrame,
        textvariable=unformatedMACAddress,width=17)
        
        MACEntry = self.MACEntry
        MACEntry.grid(column=1, row=0)
        MACEntry.focus_set()

        self.inputLabel = ttk.Label(masterFrame, text='Enter a MAC address:')
        inputLabel = self.inputLabel
        inputLabel.grid(column=0, row=0)

        self.convertButton = ttk.Button(masterFrame, text='Convert')
        convertButton = self.convertButton
        convertButton['command'] = self.convert
        convertButton.grid(column=0, row=1)

        self.convertedMAC = ttk.Label(masterFrame, text='Your converted MAC: ')
        self.convertedMAC.grid(column=0, row=2)

        self.answerLabel = ttk.Label(masterFrame, text='')
        self.answerLabel.grid(column=1, row=2)

        self.resetButton = ttk.Button(masterFrame, text='Reset')
        resetButton = self.resetButton
        resetButton.grid(column=1, row=1)
        resetButton['command'] = self.reset

    def convert(self):
        '''
        Obtain user input and convert the MAC
        '''

        unformatedMACAddress = self.MACEntry.get()

        if len(unformatedMACAddress) == 12:
            # The MAC is simply missing delimiters
            answer = address_with_no_delimiters(unformatedMACAddress)
            self.answerLabel['text'] = answer
        elif (len(unformatedMACAddress) < 12) or (len(unformatedMACAddress) < 17):
            self.answerLabel['text'] = 'Input must be 12 to 17 characters!'
        elif unformatedMACAddress[4] == ".":
            # The MAC is formated with two "."

            answer = address_with_periods(unformatedMACAddress)
            self.answerLabel['text'] = answer
        else:
            # Assumption: The last possiblity is a "-" delimited MAC

            answer = five_delimiters(unformatedMACAddress)
            self.answerLabel['text'] = answer

        # We will be nice and copy the answer to the clipboard
        self.masterFrame.clipboard_clear()
        self.masterFrame.clipboard_append(answer)

    def reset(self):
        '''
        Reset the GUI for another round of input.
        '''

        self.MACEntry.delete(0, END)
        self.MACEntry.focus_set()
        self.answerLabel['text'] = ''

def address_with_no_delimiters(unformatedMACAddress):
    '''
    If the MAC has no delimiters, we just need to insert them.
    '''
    
    MACAddress = ""
    counter = 0
    placement = 0
    
    while counter < 5:
        # We need to add the : at the correct place
        
        MACAddress += unformatedMACAddress[counter*2:(counter*2)+2] + ":"
        counter += 1

    # Exit the loop early to prevent an extra : and add last 2 octets
    MACAddress += unformatedMACAddress[10:13]

    return MACAddress

def address_with_periods(unformatedMACAddress):
    '''
    We need to strip the "."
    '''

    unformatedMACAddress = unformatedMACAddress.replace(".", "", 2)
    MACAddress = address_with_no_delimiters(unformatedMACAddress)
    return MACAddress

def five_delimiters(unformatedMACAddress):
    '''
    Replace the delimiters in unformatedMACAddress with colons
    '''

    delimiter = unformatedMACAddress[2]
    result = unformatedMACAddress.replace(delimiter, ":")
    return result

def main():
    '''
    This is the function constructs the interface.
    '''

    root = Tk()
    interface = GUI(root)
    root.mainloop()

if __name__ == '__main__':

    main()
