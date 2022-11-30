import sys
import tl_lexer


def run_lexer(data):
    # my_input = "function count_even_numbers(A: List): Number => { let even_count: Number = 0; for (i, v of A) { if (v % 2 == 0) { even_count = even_count + 1; } } return even_count; }"

    tl_lexer.lexer1.input(data)
    while True:
        tok = tl_lexer.lexer1.token()
        if not tok:
            break
        print(tok)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            data = f.read()
        run_lexer(data)
