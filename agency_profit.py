plane_company_name = input()
ticket_count_adults = int(input())
ticket_count_kids = int(input())
price_tickets_addult = float(input())
price_customer_service = float(input())

net_price_kids = price_tickets_addult * 0.30
price_ticket_addult_after_cs = price_tickets_addult + price_customer_service
price_ticket_kid_after_cs = net_price_kids + price_customer_service
total_price_tickets = ticket_count_adults * price_ticket_addult_after_cs + ticket_count_kids * price_ticket_kid_after_cs

profit = total_price_tickets * 0.20

print(f"The profit of your agency from {plane_company_name} tickets is {profit:.2f} lv.")
