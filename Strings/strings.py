name = "Bob"

greeting = "hello, bob"
print(greeting)
greeting = f"shut up {name}"
print(greeting)

#  another kind of formatting
name2 = "Pranav Rana"
greeting2 = "hello, {}, SIR !!!"
with_name = greeting2.format(name2)
print(with_name)

# For longer phrases
longer_phase = "Hello {}, Today is {}, Enjoy the day !!!"
with_name_long = longer_phase.format(name2, "Tuesday")
print(longer_phase)
