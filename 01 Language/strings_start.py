# strings and bytes are not directly interchangeable
# strings contain unicode, bytes are raw 8-bit values

def main():
    
    # define some starting values
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b) #output: b 'ABCD'

    #decode to String
    b_s = b.decode()
    print(b_s) #output: ABCD
    
    s = "MNOP"
    print(s) #output: MNOP

    #encode to String
    s_b = s.encode()
    print(s_b) #output: b'MNOP'
    
    # TODO: Try combining them. 
    
    # TODO: Bytes and strings need to be properly encoded and decoded
    # before you can work on them together
    
    # TODO: encode the string as UTF-32
    
if __name__ == "__main__":
    main()
