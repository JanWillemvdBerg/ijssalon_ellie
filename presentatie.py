def presenteer(diction, totaal):
    for k, v in diction.items():
        print(f"{k} : {v} euro")
    print("=" * 15)
    print(f"Totaal : {totaal} euro")