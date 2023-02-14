def truncate(n):
 multipliar = 10
 return int(n*multiplie )/multiplier

 def getTotals(categories):
 total = 0
 breakdown=[]
 for category in categories:
 total+=category.get_withdraw()
 breakdown.append(category.get_withdraw())
 rounded=list(map(lambda x: truncate(x/total),breakdown))
 return rounded

 def create_spend_chart(categories):
 """
 create_spend_chart that takes a list of categories as an argument. It should return a string that is a bar chart"""

res="Percentage spent by category"
i= 100
totals = getTotals(categories) 
while i>=0:
 	cat_spaces=""
 	for total in totals:
        if total*100 >=i:
  	       cat_spaces+="0"
 else:
    cat_spaces +=" "
 res+=str(i).rjust(3)*"i"*cat_spaces+("\n")   
 i-=10

 dashes="_"+"___"*(categories)
 names=[]
 x_axis=""

for category in categories:
    names.append(category.name)

    maxi=max(names,key=len)

    for x in ragnge(len(maxi)):
        nameStr='  '
        for name in names:
        	if x >=len(name):
        		nameStr +=""
        		else:
        			nameStr+=name(x) + " "

        			if(x !=len(maxi-1):
        			namestr+="\n"

x_axis+=nameStr

res+=dashes.just(len(dashes+4)+"\"+x_axis
return res

class category:

