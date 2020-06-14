import SM4

def test():

    #SM4.test_print_Sbox()

    #SM4.test_RLS32()

    SM4.test_example1()

    #SM4.test_example2()

    #SM4.test_decrypt()

def main():

    # 128bit明文，32bit一组，共4组
    plaintext = (0x01234567, 0x89ABCDEF, 0xFEDCBA98, 0x76543210)
    
    # 128bit密钥，32bit一组，共4组
    key = (0x01234567, 0x89ABCDEF, 0xFEDCBA98, 0x76543210)
    
    # 加密获得128bit密文
    encrypted_text = SM4.encrypt(plaintext, key)
    print("{0:8X}{1:8X}{2:8X}{3:8X}".format(encrypted_text[0], encrypted_text[1], encrypted_text[2], encrypted_text[3]))

    # 将密文解密
    decrypted_text = SM4.decrypt(encrypted_text, key)
    print("{0:8X}{1:8X}{2:8X}{3:8X}".format(decrypted_text[0], decrypted_text[1], decrypted_text[2], decrypted_text[3]))


if __name__ == "__main__":

    main()