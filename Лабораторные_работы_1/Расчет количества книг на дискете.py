# TODO Найдите количество книг, которое можно разместить на дискете
inf_volume = 1.44
number_of_page = 100
number_of_lines = 50
symbols_in_line = 25
weight_one_symbol = 4
kylobyte = 1024
megabyte = 1024

weight_of_symbols = weight_one_symbol * symbols_in_line * number_of_lines * number_of_page
weight_in_megabyte = weight_of_symbols / kylobyte / megabyte
number_of_books = inf_volume // weight_in_megabyte

print("Количество книг, помещающихся на дискету:", int(number_of_books))
