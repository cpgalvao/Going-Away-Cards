#["See-Mong Tan", "Victoria Kirst", "Matthew Levine", "Eric Breck", "Riccardo Crepaldi"]
# Your result should be a dictionary looking like this:
#{
# "See-Mong Tan":"Thank You! Your friends, Victoria Kirst, Matthew Levine, Eric Breck, Riccardo Crepaldi",
# "Victoria Kirst":"Thank You! Your friends, See-Mong Tan, Matthew Levine, Eric Breck, Riccardo Crepaldi",
# "Matthew Levine":"Thank You! Your friends, See-Mong Tan, Victoria Kirst, Eric Breck, Riccardo Crepaldi",
# "Eric Breck":"Thank You! Your friends, See-Mong Tan, Victoria Kirst, Matthew Levine, Riccardo Crepaldi",
# "Riccardo Crepaldi":"Thank You! Your friends, See-Mong Tan, Victoria Kirst, Matthew Levine, Eric Breck"
#}

def everyone_sign(names):
    dict = {}
    for name in names:
        message = 'Thank you! Your friends'
        for name2 in names:
            if name != name2:
                message += ', ' + name2
        dict[name] = message
        print(message)
        print(dict)
    return dict

everyone_sign(["See-Mong Tan", "Victoria Kirst", "Matthew Levine", "Eric Breck", "Riccardo Crepaldi"])