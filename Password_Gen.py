import random as rand
import clipboard as cb

# pswd chars range(33 - 126) ASCII
# special chr 33 - 47, 58 - 64, 91 - 96, 123 - 126
# numbers     48 - 57
# Upper case  65 - 90
# Lower case  97 - 122

Acct = input('Acc name: ')
user = input('Username: ')
print('Default is 128')
pwdL = input('pswd len: ')

pswd = ''

pswd += chr((rand.randint(33, 47) or rand.randint(58, 64) or rand.randint(91, 96) or rand.randint(123, 126)))
pswd += chr(rand.randint(48, 57))
pswd += chr(rand.randint(65, 90))
pswd += chr(rand.randint(97, 122))

for _ in range(int(pwdL) - 4):
    pswd += chr(rand.randint(33, 126))

cb.copy(pswd)

try:
    file = open(rf"C:\Users\%User%\OneDrive\Personal Vault\Passwords\{Acct}-{user}.txt", 'w')
    file.write(pswd)
    file.close()
except Exception as e:
    print('#############################')
    print('#############################\n')
    print('Vault is Locked')
    print('Unlock Vault and try again.\n')
    print('#############################')
    print('#############################')
