main_string = "Hello, welcome to the world of Python!"
sub_string = "welcome"
is_substring = sub_string in main_string
print(f"'{sub_string}' is {'a' if is_substring else 'not a'} substring of '{main_string}'")
