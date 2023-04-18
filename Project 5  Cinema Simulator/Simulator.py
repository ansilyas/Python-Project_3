#%%
films={
    "Sword Art Online":[7,6],
    "One punch":[10,6],
    "My Hero":[5,5],
    "Tarzan":[12,3],
    "God of High School":[12,3]
}
while True:
    choice=input("What Film would you like to Watch?: ").strip().title()
    if choice in films:
        age=int(input("How old are you?: ").strip())
        if age>=films[choice][0]: 
            num_seats=films[choice][1]
            if num_seats>0:
                print("Enjoy the film!")
                films[choice][1]=films[choice][1]-1
            else:
                print("Sorry, we are sold out!")
        else:
          print("You are to young to see that film!")
    else:
        print("We don't have the film...")


# %%
