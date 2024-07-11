from textnode import Textnode


def main():
    node = Textnode("This is a text node", "bold", "https://www.boot.dev")
    print(node)


#main() 

props = {
    "href": "https://www.google.com", 
    "target": "_blank",
    }

for key in props.keys():
    print(key + " ", props[key], end=" ")


