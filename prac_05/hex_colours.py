
COLOURS_TO_HEX = {"absolutezero": "#0048ba", "apricot": "#fbceb1", "ashgrey": "b2beb5", "amethyst": "9966cc",
                 "bitterlime": "bfff00", "bittersweet": "#fe6f5e", "bananayellow": "ffe135", "brightube": "d19fe8",
                 "camel": "c19a6b", "celeste": "b2ffff"}


colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
    print(f"The code for \"{colour_name}\" is {COLOURS_TO_HEX.get(colour_name)}")
    colour_name = input("Enter a colour name: ").lower()


