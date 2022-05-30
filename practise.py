def calculate_park_profits(paid_parking_count, event_ticket_count, trash_can_count):
    """
    The function accepts following parameters:
        paid_parking_count: INTEGER_ARRAY, The number of people who paid for parking at each park.
        event_tickets: INTEGER_ARRAY, The number of event tickets each park sold.
        trash_can_count: INTEGER_ARRAY, The number of trash cans maintained by each park.
    """

    # Write your code here
    total_profit=[]
    find_max=0
    index=-1
    profit_to_park={}
    for i in range(0,len(event_ticket_count)):
        parking=paid_parking_count[i]*10
        ticket=event_ticket_count[i]*20
        trash=trash_can_count[i]*15
        profit=parking+ticket-trash
        if profit in profit_to_park:
            profit_to_park.get(profit).append(i)
        else:
            profit_to_park[profit]=[i]
        #part1
        if profit>find_max:
            find_max=profit
            index=i
        total_profit.append(profit)
    print(index+1)
    print(paid_parking_count[index]*10+event_ticket_count[index]*20)
    print(trash_can_count[index]*15)

    #part2
    #income+maintenance cost
    print(find_max)
    temp=profit_to_park.get(find_max)

    for i in range(0, len(total_profit)):
        if total_profit[i]==find_max:
            print("Park #",i+1, "+$", paid_parking_count[i]*10," from parking fees +$", event_ticket_count[i]*20," from special event tickets -$", trash_can_count[i]*15, " from garbage maintenance")

    for i in range(0,len(temp)):
        print("Park #",temp[i]+1, "+$", paid_parking_count[temp[i]]*10," from parking fees +$", event_ticket_count[temp[i]]*20," from special event tickets -$", trash_can_count[temp[i]]*15, " from garbage maintenance")




    #part3
    #adjust calculation and print how much park saved with bulk
    max_profit=0
    output=[]
    for i in range(0, len(paid_parking_count)):
        parking=paid_parking_count[i]*10
        ticket=event_ticket_count[i]*20
        trash_div=trash_can_count[i]//5*60
        trash_mod=trash_can_count[i]%5*15
        trash_cost=trash_div+trash_mod
        profit=parking+ticket-trash_cost

        if profit>max_profit:
            max_profit=profit
        output.append(profit)

    print(max_profit)
    for i in range(0, len(output)):
        if output[i]==max_profit:
            print(paid_parking_count[i]*10)
            print(event_ticket_count[i]*20)
            trash_div=trash_can_count[i]//5*60
            trash_mod=trash_can_count[i]%5*15
            trash_cost=trash_div+trash_mod
            print(trash_cost)
            print(trash_can_count[i]*15-trash_cost)


calculate_park_profits([12,20,10],[1,0,5],[6,5,5])