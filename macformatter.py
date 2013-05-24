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

        user_input = ''
        
        self.mac_entry = ttk.Entry(master_frame,
        textvariable=user_input,width=17)
        
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

        def license_window():
            '''
            Show the user license and contact information.
            '''
            #Breaking up this line impacts the formatting
            messagebox.showinfo("License", "This software is released under the GLPv2.  Please report bugs to dittmer.matthew@gmail.com")
        
        menu = Menu(my_parent)
        my_parent.config(menu=menu)

        helpmenu = Menu(menu)
        helpmenu['tearoff'] = 0
        menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About", command=license_window)

    def convert(self):
        '''
        Obtain user input and convert the MAC
        '''

        user_input = self.mac_entry.get()
        answer = ''

        if re.search('[a-f\d]{12}', user_input):
            # The MAC is simply missing delimiters
            answer = address_with_no_delimiters(user_input)
            self.answer_label['text'] = answer
        elif re.search("([a-f\d]{2}[\.\s:-]){5}([a-f\d]{2})", \
                       user_input, re.IGNORECASE):
            # The input has five delimiters.
            answer = five_delimiters(user_input)
            self.answer_label['text'] = answer            
        elif re.search('([a-f\d]{4}[\.]){2}([a-f\d]{4})', \
                       user_input, re.I):
            # The MAC is formated with two "."
            answer = address_with_periods(user_input)
            self.answer_label['text'] = answer
        else:
            # The input is invalid
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

def address_with_no_delimiters(user_input):
    '''
    If the MAC has no delimiters, we just need to insert them.

    >>> address_with_no_delimiters("012345678910")
    '01:23:45:67:89:10'
    >>> 
    >>> address_with_no_delimiters("abcdef012345")
    'ab:cd:ef:01:23:45'
    '''
    
    mac_address = ""
    counter = 0
    
    while counter < 5:
        # We need to add the : at the correct place
        
        mac_address += user_input[counter*2:(counter*2)+2] + ":"
        counter += 1

    # Exit the loop early to prevent an extra : and add last 2 octets
    mac_address += user_input[10:13]

    return mac_address

def address_with_periods(user_input):
    '''
    Strip the "." and add ":" delimiters.
    This fuction depends on address_with_no_delimiters()

    >>> address_with_periods("0123.4567.8910")
    '01:23:45:67:89:10'
    >>> 
    >>> address_with_periods("abce.ef67.8910")
    'ab:ce:ef:67:89:10'
    '''

    user_input = user_input.replace(".", "", 2)
    mac_address = address_with_no_delimiters(user_input)
    return mac_address

def five_delimiters(user_input):
    '''
    Replace the delimiters in user_input with colons

    >>> five_delimiters("01.23.45.67.89.10")
    '01:23:45:67:89:10'
    >>> five_delimiters("01-23-45-67-89-10")
    '01:23:45:67:89:10'
    '''

    delimiter = user_input[2]
    result = user_input.replace(delimiter, ":")
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
