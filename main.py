"""
Name:
Date:
Brief Project Description:
GitHub URL:
"""
import kivy
kivy.require('1.8.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from booklist import BookList

# Create your main program in this file, using the ReadingListApp class


class ReadingListApp(App):
    def __init__(self, **kwargs):
         self.list = BookList()
         self.list.loadBook()


    def build(self):
        """
        Build the Kivy GUI
        :return: reference to the root Kivy widget
        """
        self.title = "Reading List 2.0"
        self.root = Builder.load_file('app.kv')
        self.create_entry_buttons('r')
        return self.root

    '''
    
    '''
    def create_book_buttons(self, s):
        self.root.ids.view.listview.clear_widgets()
        chosen = self.list.choseBookByStatus(s)
        for book in chosen.getBooks():
            temp_button = Button(text=book.getTitle(), size_hint_y=0.8/chosen)
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.view.listview.add_widget(temp_button)
        header = "Total pages "
        if (s == 'c'):
            header += 'completed'
            self.root.ids.footer_status.text = "Click one book to see details"
        else:
            header += 'to read'
            self.root.ids.footer_status.text = "Click books to mark them as completed"
        header += ': ' + chosen.getTotalPage()
        self.root.ids.header_status.text = header


    def press_entry(self, instance):
        name = instance.text
        book = self.list.getBookByTitle(name)
        if(book.getStatus() == 'r'):
            book.markComplete()
        instance.state = 'down'

    def press_clear(self):
        self.root.ids.title.text = ''



    def press_add(self):
        if (self.getInputString(self, self.root.ids.title.text)
                and self.getInputString(self.root.ids.author.text)
                and self.getInputInt(self.root.ids.page.text)):
            self.list.addBook(self.root.ids.title.text, self.root.ids.author.text, self.root.ids.page.text, 'r')
            self.press_clear()
            self.create_book_buttons(self, 'r')


    # validate string input
    def getInputString(self, inputStr):

        if (len(inputStr) == 0):
            self.root.ids.view.footer_status.text = ("All fields must be completed")
            return False
        else:
            return True

    # validate integer input
    def getInputInt(self, intInput):
        try:
            num = int(intInput)
        except ValueError:
            self.root.ids.view.footer_status.text = ("Please enter a valid number")
            return False
        else:
            if num >= 0:
                return True
            else:
                self.root.ids.view.footer_status.text = ("Number must be >= 0")
                return False

ReadingListApp().run()



