print("welcome to pizza! what would you like to order, here is our menu")
print("Pizza sold at £7.30")
print("Pie sold at £3.45")
print("Burger sold at £4.50")
print("Chips sold at £2.00")
print("Onion rings ordered at £2.30")
print("A drink at £1.50")

menu = ['pizza','pie','burger','chips','onion_rings','drink']
total = 0
order = []
pizza = 7.30
pie = 3.45
burger = 4.50
chips = 2.00
onion_rings = 2.30
drink = 1.50

print("Say" + " stop" + " to finalise your order")

count = 0
while count == 0:
    print("Add an item to your basket from the menu...: ")
    choice = input().lower() 
    order.append(choice)
    if choice == "stop":
        count += 1
   
            
    
    
order.remove("stop")
     
for x in order:
    if x == "pizza":
        total += float(pizza)
    elif x == "pie":
        total += float(pie)
    elif x == "burger":
        total += float(burger)      
    elif x == "chips":
        total += float(chips)
    elif x == "onion rings":
        total += float(onion_rings)  
    elif x == "drink":
        total += float(drink)    
   

print(f"Your total is {total}")

print(f"here is your order {order}")
