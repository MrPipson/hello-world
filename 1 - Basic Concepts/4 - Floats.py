
# Floats are used to represent non-integer numbers e.g. 0.5 and -7.8237591

3 / 4
9.87321

# Computers can't store floats perfectly accurately, in the same way that we can't write down the
# complete decimal expansion of 1/3 (0.3333333333333333...).
# Keep this in mind, because it often leads to infuriating bugs!


8 / 2 # division of 2 integers produces a float
6 * 7.0 # multiplication of integer and a float produces a float
6 + 1.65 # addition of integer and a float produces a float since Python implicitly converts the integer into float

# Implict conversion of integer to float is rare, it's better to code for conversion
