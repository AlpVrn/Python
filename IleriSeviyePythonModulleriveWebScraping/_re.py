import re

result = dir(re)

# re module
str = "Python Kursu : Pyton Programlama Rehberi |40 saat"

# re.findall()

# result = re.findall("Python",str)
# result = len(result)

# re.split()

result = re.split(" ",str)
result = re.split("R",str)

#re.sub()

# result = re.sub(" ","-",str) # ilk başta yazılan değeri sonradan girilen değerle değiştirir
result = re.sub("\s","-",str)

#re.search

result = re.search("Python",str)

# result = result.span()
# result = result.start()
# result = result.end()
# result = result.group()
result = result.string

# regular expression
"""
[] - Köşeli parantezler arasında yazılan bütün karakterler
     aranır

     [abc] => a : 1 match
     ac      ac : 2 match
         Python : No Match

    [a-e] => [abcde]
    [1-5] => [12345]
    [0-39] => [01239] 

    [^abc] => abc dışındaki karakterler.
    [^0-9] => rakam olmayan karakterler
"""
result = re.findall("[abc]",str)
result = re.findall("[sat]",str)
result = re.findall("[a-z]",str)
result = re.findall("[0-5]",str)
result = re.findall("[0-39]",str)
result = re.findall("[^abc]",str)
result = re.findall("[^0-9]",str)

"""
    . - Herhangi bir tek karkateri belirtir.

        ** =>  a     : No match
               ab    : 1 Match
               abc   : 1 Match 
               aabcd : 2 Match  
"""

result = re.findall("...",str)
result = re.findall("Py..on",str)
result = re.findall("Py..on",str)

"""
    ^  - Belirtilen string karakterle başlıyor mu ?

    ^a => a:    1 match
          abc:  1 match
          bac:  No match  
"""

result = re.findall("^P",str)

"""
    $ - Belirtilen karakterle bitiyor mu?
    a$ => a      : 1 match
          lamba  : 1 Match
          Python : No Match    
"""

result = re.findall("t$",str)
result = re.findall("saat$",str) 
result = re.findall("saatt$",str)

"""
    * - Bir karakterin sıfır ya da dah fazla sayıda olmasını
    kontrol eder.
    ma*n => mn      : 1 match
            man     : 1 match
            maaan   : 1 match
            main    : No Match (a' nın arkasına n gelmiyor.)
"""

result = re.findall("sa*t",str) # Burda birden fazla a olabilir (illa t nin arkasında a olması gerekiyor yoksa çalışmaz)

""" 
    + - Bir karakterin bir ya da daha fazla olmasını
        kontrol eder

        ma+n => mn      : No Match
                man     : 1 Match
                maaan   : 1 match 
                main    : No match (a'nın arkasına gelmiyor)
"""

result = re.findall("sa+at",str) # Burda bir tane  a olabilir (illa t nin arkasında a olması gerekiyor yoksa çalışmaz)

"""
     + - Bir karakterin bir ya da hiç olmasını
        kontrol eder

        ma?n => mn      : No Match
                man     : 1 Match
                maaan   : 1 match 
                main    : No match (a'nın arkasına gelmiyor)
"""
result = re.findall("sa?t",str)


"""
    {} - Karakter sayısını kontrol eder.

        al{2}   => a karakterinin arkasına 1 karakteri 2 kez tekrarlanmalı.
        al{2,3} => a karakterini arkasına 1 karakteri en az 2 en fazla 3 kez tekrarlanmalıdır
        [0-9],{2,4} => en az 2 en çok 4 basamaklı sayılar
"""

result =re.findall("a{2}", str)
result = re.findall("[0-9]{2}",str)

"""
    | - altarnetif seçeneklerden birinin gerçekleşmsi gerekir.

        a|b => a yada b

            cde => no match
            ade => 1 match
            acdbea => 3 match
"""

"""
    () - gruplamak için kullanılır.

        (a|b|c)xz => a,b,c karakterlerinin arkasına xz gelmelidir 
"""



"""
    \ - Özel karakterleri aramamızı sağlar.
        \$a => $ karakterlerinin arkasına a karakterinin arar. Yani
               $ regular exp. engine tarafından yorumlanmaz.

        \A - Belirtilen karakter string in başında mı ?
             \Athe => the string i başında mı

                result = re.findall("\APython",str)
                result = re.findall("saat\Z",str)
        
        \Z - Belirtilen karakter string in sonunda mı ? 
             \bthe => the kelimenin başında mı?
             the\b => the kelimenin sonunda mı?

        \b - Belirtilen karakter kelimenin başında ya da sonunda mı ?
            \bthe => the kelimenin başında mı ? 
            the\b => the kelimenin sonunda mı ?
        
        \B - Belirtilen karakter kelimenin başında ya da sonunda değil mi ? 
             \Bthe => the kelimenin başında diğil mi

        \d - [0-9] ile aynı anlama gelir yani rakamları arar.
             \d =>12abc34
        
        \D - [^0-9] ile aynı anlama gelir yani rakam olmayanları arar
             \D => 1ab44_50
        
        \s - Boşluk karakterlerini arar.
        \S - Boşluk karakterleri dışındakiler
        \w - Alfabetik karakterler, rakamlar ve alt çizgi karakterleri.
        \W - \w nin tam tersi
"""

print(result)