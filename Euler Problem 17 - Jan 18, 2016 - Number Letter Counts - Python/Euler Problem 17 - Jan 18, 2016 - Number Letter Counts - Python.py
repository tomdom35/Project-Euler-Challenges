one = 'one'
two = 'two'
three = 'three'
four = 'four'
five = 'five'
six = 'six'
seven = 'seven'
eight = 'eight'
nine = 'nine'
ten = 'ten'
eleven = 'eleven'
twelve = 'twelve'
thirteen = 'thirteen'
fourteen = 'fourteen'
fifteen = 'fifteen'
sixteen = 'sixteen'
seventeen = 'seventeen'
eighteen = 'eighteen'
nineteen = 'nineteen'
twenty = 'twenty'
thirty = 'thirty'
forty = 'forty'
fifty = 'fifty'
sixty = 'sixty'
seventy = 'seventy'
eighty = 'eighty'
ninety = 'ninety'
hundred = 'hundred'
thousand = 'thousand'

nums = [
'',
'one',
'two',
'three',
'four',
'five',
'six',
'seven',
'eight',
'nine',
'ten',
'eleven',
'twelve',
'thirteen',
'fourteen',
'fifteen',
'sixteen',
'seventeen',
'eighteen',
'nineteen']

nums2 = [
'',
'',
'twenty',
'thirty',
'forty',
'fifty',
'sixty',
'seventy',
'eighty',
'ninety',
'hundred',
'thousand']

def getWordForm(num,nums,nums2):
    if(num<20):
        return len(nums[num])
    elif(num/10 < 10):
        return len(nums2[int(num/10)] + nums[num%10])
    elif(num/100<10):
        n = getWordForm(num%100,nums,nums2)
        return len(nums[int(num/100)] + 'hundredand')+n
    else:
        return len('onethousand')
        
        

total = 0
for i in range(1,1001):
    total+=getWordForm(i,nums,nums2)
print(total-(9*3))










    
    
