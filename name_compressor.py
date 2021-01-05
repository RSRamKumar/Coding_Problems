"""
Given a full name, compress it as shown:
"Anna Butler" => "Anna B."
"Anna Butler Corey => "Anna B.C."
"""

def name_compressor(full_name):
    full_name_list_format = full_name.split()
    #print(full_name_list_format[0] +" "+ " ".join([i[0] for i in full_name_list_format[1:]]))
    return full_name_list_format[0] + " " +  ".".join("".join([i[0] for i in full_name_list_format[1:]])) + "."

def main():
    full_name_list=["Ackshay Ruppa Surulinathan","Anna Butler","Lisa	Henderson","Jessica	Alsop","Ian	Miller",]
    compressed_name_list = list(map(name_compressor,full_name_list))
    print(compressed_name_list)

if __name__ == '__main__':
    main()
