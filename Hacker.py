import os
import random
import time

def loading(fill):
    os.system('cls')
    percent = int(fill/100 * 39)
    print('Hashing Username CheckSUM...  Please Wait')
    print(' ---------------------------------------')
    print(' ', end="")
    print('*'*percent, end="")
    print(' '*(39-percent), '=   ',int(fill))
    print(' ---------------------------------------')
    time.sleep(2)

    
def skullsigprint():
    print('                             ud$$$**$$$$$$$bc.                          ')
    print('                          u@**"        4$$$$$$$Nu                       ')
    print('                        J                ""#$$$$$$r                     ')
    print('                       @                       $$$$b                    ')
    print('                     .F                        ^*3$$$                   ')
    print('                    :% 4                         J$$$N                  ')
    print('                    $  :F                       :$$$$$                  ')
    print('                   4F  9                       J$$$$$$$                 ')
    print('                   4$   k             4$$$$bed$$$$$$$$$                 ')
    print('                   $$r  F            $$$$$$$$$$$$$$$$$r                ')
    print('                   $$$   b.           $$$$$$$$$$$$$$$$$N                ')
    print('                   $$$$$k 3eeed$$b    $$$Euec."$$$$$$$$$                ')
    print('    .@$**N.        $$$$$" $$$$$$FL $$$$$$$$$$$  $$$$$$$                ')
    print('    :$$L  .L       $$$$$ 4$$$$$$  * $$$$$$$$$$F  $$$$$$F         edNc   ')
    print('   @$$$$N  ^k      $$$$$  3$$$$*%   $F4$$$$$$$   $$$$$"        d"  z$N  ')
    print('   $$$$$$   ^k     $$$"   #$$$F   .$  $$$$$c.u@$$$          J"  @$$$$r ')
    print('   $$$$$$$b   *u    ^$L            $$  $$$$$$$$$$$$u@       $$  d$$$$$$ ')
    print('    ^$$$$$$.    "NL   "N. z@*     $$$  $$$$$$$$$$$$$P      $P  d$$$$$$$ ')
    print('       ^"*$$$$b   .*L   9$E      4$$$  d$$$$$$$$$$$"     d*   J$$$$$r   ')
    print('            ^$$$$u  .$.  $$$L     "#" d$$$$$$".@$$    .@$"  z$$$$*"     ')
    print('              ^$$$$. ^$N.3$$$       4u$$$$$$$ 4$$$  u$*" z$$$"          ')
    print('                *$$$$$$$$ *$b      J$$$$$$$b u$$P $"  d$$P             ')
    print('                   #$$$$$$ 4$ 3*$"$*$ $"$c@@$$$$ .u@$$$P               ')
    print('                     "$$$$  ""F~$ $uNr$$$^&J$$$$F $$$$#                 ')
    print('                       "$$    "$$$bd$.$W$$$$$$$$F $$"                   ')
    print('                         ?k         ?$$$$$$$$$$$F*                     ')
    print('                          9$$bL     z$$$$$$$$$$$F                       ')
    print('                           $$$$    $$$$$$$$$$$$$                        ')
    print('                            .#$$c  .$$$$$$$$$"                          ')
    print('                             .@"#$$$$$$$$$$$$b                          ')
    print('                           z*      $$$$$$$$$$$$N.                       ')
    print('                         e"      z$$"  #$$$k  *$$.                     ')
    print('                     .u*      u@$P"      #$$c   $$c                   ')
    print('              u@$*"""       d$$"            "$$$u  ^*$$b.               ')
    print('            :$F           J$P"                ^$$$c   "$$$$$$bL        ')
    print('           d$$  ..      @$#                      #$$b         #$       ')
    print('           9$$$$$$b   4$$                          ^$$k         $      ')
    print('            "$$6""$b u$$                             $    d$$$$$P      ')
    print('              $F $$$$$"                              ^b  ^$$$$b$       ')
    print('               $W$$$$"                                b@$$$$"         ')
    print('                                                        ^$$$* FBHack101.2')


def main():
    os.system('color A')
    os.system('title FBHack by STP')
    os.system('cls')
    skullsigprint()
    key = input('Enter Facebook Username:')
    os.system('cls')

    i = 0
    while i < 100:
        loading(i)
        i += random.choice(range(1,20))

    loading(100)
    input('Key Loaded, press any key to begin decryption')

    while True:
        print(random.choice(range(1000,10000)), end=' ')
        
main()

