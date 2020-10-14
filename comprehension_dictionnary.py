touch_key = "K_SPACE"
def change_letter(arg):
    print(f"changement de H en {arg}")

touch_functions = {
    "K_SPACE" : change_letter,
}

(touch_functions["K_SPACE"]("argument") for key in touch_functions if key == touch_key)
# for key in touch_functions:

#     if key == touch_key:
#         touch_functions["K_SPACE"]("argument")