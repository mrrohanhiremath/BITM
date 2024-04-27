A='''mango city triple single qts'''

B="""mango city triple double qts"""

C="mango city double qts"

D='mango city single qts'

E="mango's city - use single qts inside double qts"

F='mango"s city - use single qts inside double qts'

G='mango\'s city - use slash single qts inside double qts'

H="mango\"s city - use slash double qts inside double qts"

I="mango\s city - use slash inside double qts"

J="mango\n s city - use new line inside double qts"

K="mango\t s city - use tab space inside double qts"

L="mango\b s city - use backspace inside double qts"

M="mango\\ s city - use double slashes inside double qts"



N='''mangos \
city - use \
single qts \
inside double qts'''


O='''mangos 
city - use 
single qts 
inside double qts'''

P="mango\\ s city - use double slashes inside double qts"
print(P)

P="mango\\\\ s city - use double slashes inside double qts"
print(P)

P="mango\\\\\\ s city - use double slashes inside double qts"
print(P)

P="mango\\\\\\\\ s city - use double slashes inside double qts"
print(P)




ui=input('enter the string')
print([w for w in ui.split() if 's' in w])


