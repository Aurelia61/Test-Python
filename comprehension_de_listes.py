class Seed():
    """
        Model for seed table in database "P2"
    """

    def __init__(self, id, name, quantity, seed_period):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.seed_period = seed_period
        self.grown = False

    def __str__(self):
        """
            Overload the print method
        """

        return f"N°{self.id} :: {self.name} - Quantité :: {self.quantity}"

    def to_grow(self):
        self.grown = True



if __name__ == "__main__":
    seeds=[]
    seed_1 = Seed(2, "berry", 3, 6)
    seeds.append(seed_1)
    seed_2 = Seed(3, "apple", 5, 10)
    seeds.append(seed_2)
    seeds.append(Seed(5, "banana", 4, 2))
    seeds.append(Seed(16, "berry", 50, 12))
    
    # print("\nListe des graines :: ")
    # for item in seeds:
    #     print(f"{item.name} : {item.quantity} - {item.grown}")
    banana_t1 = [my_seed for my_seed in seeds if my_seed.name == "banana"][0]
    print(f"\ntest banana n°1 → \n{banana_t1}")

    banana_t2 = [my_seed for my_seed in seeds if my_seed.name == "banana"]
    print(f"\ntest banana n°2 (sans le [0]) → \n{banana_t2}")

    try:
        banana_t3 = [my_seed for my_seed in seeds if my_seed.name == "banana"][1]
        print(f"\ntest banana n°3 (avec [1]) → \n{banana_t3}")
    except IndexError:
        print("\nLe test banana n°3 (avec [1]) provoque une erreur, car il n'y a qu'une seule fois banana dans la liste seeds")

    banana_t4 =  [my_seed.name for my_seed in seeds if my_seed.name == "banana"][0]
    print(f"\ntest banana n°4 (my_seed.name)→ \n{banana_t4}")

    banana_t5 =  [my_seed.name.upper() for my_seed in seeds if my_seed.name == "banana"][0]
    print(f"\ntest banana n°5 (my_seed.name.upper())→ \n{banana_t5}")

    banana_t6 =  [my_seed.quantity*2 for my_seed in seeds if my_seed.name == "banana"][0]
    print(f"\ntest banana n°6 (my_seed.quantity*2)→ \n{banana_t6}")
    
    banana_t7 =  [[my_seed.name, my_seed.grown] for my_seed in seeds if my_seed.name == "banana"][0]
    print(f"\ntest banana n°7 ([my_seed.name, my_seed.grown])→ \n{banana_t7}")

    berry_t1 = [my_seed for my_seed in seeds if my_seed.name == "berry"][0]
    print(f"\ntest berry n°1 (avec [0]) → \n{berry_t1}")

    berry_t2 = [my_seed for my_seed in seeds if my_seed.name == "berry"]
    print(f"\ntest berry n°2 (sans [0]) → \n{berry_t2}")

    berry_t3 = [my_seed for my_seed in seeds if my_seed.name == "berry"][1]
    print(f"\ntest berry n°3 (avec [1]) → \n{berry_t3}")


print("")