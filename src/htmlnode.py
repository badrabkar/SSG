class HTMLNode:
    def __init__(self, tag:str = None, value:str = None, children: list = None, props:dict = None) -> None:
        self.tag = tag; # A string representing the HTML tag
        self.value = value; # The value of the HTML tag
        self.children = children; # A list of HTMLNode objects representing the children of this node
        self.props = props; # props - A dictionary of key-value pairs representing the attributes of the HTML tag


# By raising a NotImplementedError, you clearly communicate that any 
# subclass inheriting from the base class must provide its own 
# implementation of this method. If a subclass does not override 
# the method and tries to call it, the program will raise a 
# NotImplementedError, thus enforcing the contract.

    def to_html(self) -> None:
        raise NotImplementedError("Subclass must implement abstract method")
    
    def props_to_html(self) -> str:

        string:str

        for key in self.props.keys():
            print(key + " ", self.props[key], end=" ")
            string += key
            string += "="
            string += '"'
            string += self.props[key]
            string += '"'

        return string
    
