from country_data_set import countries
while(True):
    option=input('\n 1. Show all countries \n 2. Filter by continent \n 3. Population > 10M \n 4. Most populated country \n 5. Top 5 populated countries \n 6. Exit \n')
    match option:
        case '1':
            print("data of the country we have:\n")
            for nameOfCountry in countries:
                print(nameOfCountry["name"])
        case '2':
            user=input("\nenter continent name:\n")
            for c in countries:
                if c["continent"].lower()== user.lower():
                    print(c["name"]," -> ",c["capital"])
        case '3':
            print("\ncountry population more than 10 million\n")
            for n in countries:
                if n['population']>10000000:
                    print(n["name"],"-> ",n["population"])
        case '4':
            print("\nmost populated country\n")
            most=countries[0]['population']
            name=countries[0]['name']
            for j in countries:
                if most<j['population']:
                    most=j['population']
                    name=j['name']
            print(name," -> ",most)
        case '5':
            print("\nthe top 5 populated country are\n")
            top=sorted(countries,key=lambda x : x['population'],reverse=True)
            for i in top[:5]:
                print(i['name']," -> ",i['population'])
        case '6':
            print("thank you!")
            break
    

    
