import json
with open("Chap#24(Json_File_Handling)/first.json","r") as f:
    data= json.load(f)

print("===Data of first Layer===")
print("name:",data["name"])
print("score:",data["score"])
print("Muslim?:",data["Is_Muslim"])


print("\n======Data of Nested Object======")
print("Friend Name:",data["myObj"]["name"])
print("Friend Gender:",data["myObj"]["Gender"])
print("Friend age:",data["myObj"]["age"])
print("Friend'shop items:",data["myObj"]["ShopItems"])


print("\n======Deep Layer(nested dictionary in list)======")
mango_friut=data["myObj"]["ShopItems"][0]["fruits"][1]
print("Nisa ka 2nd fruit:",mango_friut)
Dark_choclate=data["myObj"]["ShopItems"][2]["Choclates"] [1]
print("Nisa ki 2nd choclate:",Dark_choclate)