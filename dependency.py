# Class 1
class Printer:
    def print_message(self, message):
        print("Printing:", message)


# Class 2
class Computer:
    def print_document(self, printer):
        printer.print_message("Hello, World!")


# Main Program
printer = Printer()
computer = Computer()

computer.print_document(printer)
