'''
This script will convert a given MAC address to a colon delimited format.
Python 3.3
'''

from tkinter import *
from tkinter import ttk
import re

class GUI(object):
    '''
    This class will run the GUI.
    '''

    def __init__(self, my_parent):

        self.master_frame = ttk.Frame(my_parent)
        master_frame = self.master_frame
        master_frame.grid(column=0, row=0)

        unformated_mac_address = ''
        
        self.mac_entry = ttk.Entry(master_frame,
        textvariable=unformated_mac_address,width=17)
        
        mac_entry = self.mac_entry
        mac_entry.grid(column=1, row=0)
        mac_entry.focus_set()

        self.input_label = ttk.Label(master_frame, text='Enter a MAC address:')
        input_label = self.input_label
        input_label.grid(column=0, row=0)

        self.convert_button = ttk.Button(master_frame, text='Convert')
        convert_button = self.convert_button
        convert_button['command'] = self.convert
        convert_button.grid(column=0, row=1)

        self.converted_mac = ttk.Label(master_frame, \
                                       text='Your converted MAC: ')
        self.converted_mac.grid(column=0, row=2)

        self.answer_label = ttk.Label(master_frame, text='')
        self.answer_label.grid(column=1, row=2)

        self.reset_button = ttk.Button(master_frame, text='Reset')
        reset_button = self.reset_button
        reset_button.grid(column=1, row=1)
        reset_button['command'] = self.reset

    def convert(self):
        '''
        Obtain user input and convert the MAC
        '''

        unformated_mac_address = self.mac_entry.get()

        if re.search('[a-f\d]{12}', unformated_mac_address):
            # The MAC is simply missing delimiters
            answer = address_with_no_delimiters(unformated_mac_address)
            self.answer_label['text'] = answer
        elif re.search("([a-f\d]{2}[:\s-]){5}([a-f\d]{2})", \
                       unformated_mac_address, re.IGNORECASE):
            # The input has five delimiters.
            answer = five_delimiters(unformated_mac_address)
            self.answer_label['text'] = answer            
        elif re.search('([a-f\d]{4}[\.]){2}([a-f\d]{4})', \
                       unformated_mac_address, re.I):
            # The MAC is formated with two "."

            answer = address_with_periods(unformated_mac_address)
            self.answer_label['text'] = answer
        else:
            # The input is invalid

##            answer = five_delimiters(unformated_mac_address)
##            self.answer_label['text'] = answer

            self.answer_label['text'] = 'Input must be 12 to 17 characters!'

        # We will be nice and copy the answer to the clipboard
        self.master_frame.clipboard_clear()
        self.master_frame.clipboard_append(answer)

    def reset(self):
        '''
        Reset the GUI for another round of input.
        '''

        self.mac_entry.delete(0, END)
        self.mac_entry.focus_set()
        self.answer_label['text'] = ''

def address_with_no_delimiters(unformated_mac_address):
    '''
    If the MAC has no delimiters, we just need to insert them.
    '''
    
    mac_address = ""
    counter = 0
    
    while counter < 5:
        # We need to add the : at the correct place
        
        mac_address += unformated_mac_address[counter*2:(counter*2)+2] + ":"
        counter += 1

    # Exit the loop early to prevent an extra : and add last 2 octets
    mac_address += unformated_mac_address[10:13]

    return mac_address

def address_with_periods(unformated_mac_address):
    '''
    We need to strip the "."
    '''

    unformated_mac_address = unformated_mac_address.replace(".", "", 2)
    mac_address = address_with_no_delimiters(unformated_mac_address)
    return mac_address

def five_delimiters(unformated_mac_address):
    '''
    Replace the delimiters in unformated_mac_address with colons
    '''

    delimiter = unformated_mac_address[2]
    result = unformated_mac_address.replace(delimiter, ":")
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
