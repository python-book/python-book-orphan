complex_1 = 3 + 5j
match complex_1:
    case 3 as real:
        print(f"# matched real {real}.")
    case 5j as complex_literal:
        print(f"# matched complex literal {complex_literal}")
    case complex(imag = 5) as complex_:
        print(f"# matched complex {complex_}")
        # matched complex (3+5j)
    case complex(real = x, imag = (4|5|6)) as complex_:
        print(f"# matched complex 4|5|6 {complex_}")        
    case _:
        print(f"# Error.")
print(f"# used outside case clause: {complex(imag = 5)}")
# used outside match-case: 5j