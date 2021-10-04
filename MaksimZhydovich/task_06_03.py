from string import ascii_lowercase


class Cipher:
    """Class provides keyword encoding and decoding for latin alphabet"""

    def __init__(self, keyword):
        """Init Cipher and create encoding table"""
        self.__encoder, self.__decoder = self.create_decoding_table(keyword)

    @staticmethod
    def create_decoding_table(keyword):
        """Create decoding/encoding table"""
        encoder = ascii_lowercase
        decoder = keyword.lower()

        num_of_letters = 26
        for i in range(num_of_letters):
            if encoder[i] not in decoder:
                decoder += encoder[i]

        return encoder, decoder

    def encode(self, word):
        """Return encoding word"""
        result = ""
        for l in word:
            if l.isalpha():
                if l.islower():
                    result += self.__decoder[self.__encoder.index(l)]
                else:
                    result += self.__decoder[self.__encoder.index(l.lower())].upper()
            else:
                result += l

        return result

    def decode(self, word):
        """Return decoding word"""
        result = ""
        for l in word:
            if l.isalpha():
                if l.islower():
                    result += self.__encoder[self.__decoder.index(l)]
                else:
                    result += self.__encoder[self.__decoder.index(l.lower())].upper()
            else:
                result += l

        return result


def main():
    c = Cipher("crypto")
    print(c.encode("Hello world"))
    print(c.decode(c.encode("Hello world")))
    print(c.decode("Fjedhc dn atidsn"))


if __name__ == "__main__":
    main()
