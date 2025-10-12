def total(rupee: int, paisa: int):
    """
    Calculate total paisa
    """
    return rupee * 100 + paisa


#balance = [10, 50]
balance = {"rupee": 100 , "paisa": 50}
#would not work for {"rupees": 100 , "paisas": 50}, expects same argument name.

print(total(**balance), "paisa")
#this astriks unpacks balance, a list into many values. (*balance)
#for dictionary, **balance