# read the file, read each line,
# break it open, meaning split it,
# store all the attributes in different name attributes,
# has 6 attributes
# wrap it all into a function def Get_Retail_Item_Data()
def Get_Retail_Item_Data():

    file_object = open("RetailStoreItemData.txt", "r")

    Retail_Items = []

    first_line = True

    for eachLine in file_object:

        if first_line == True:
            first_line = False
            continue

        eachLine = eachLine.strip()

        a = eachLine.split(",")

        Item_UPC = a[0]

        # some rows have 7 columns
        if len(a) == 7:
            Item_Description = a[1]
            Item_Max_Qty = int(a[2])
            Item_Order_Threshold = int(a[3])
            Item_Replenishment_Order_Qty = int(a[4])
            Item_On_Hand = int(a[5])
            Item_Unit_Price = float(a[6])

        # some rows have 8 columns
        elif len(a) == 8:
            Item_Description = a[1] + "," + a[2]
            Item_Max_Qty = int(a[3])
            Item_Order_Threshold = int(a[4])
            Item_Replenishment_Order_Qty = int(a[5])
            Item_On_Hand = int(a[6])
            Item_Unit_Price = float(a[7])

        Retail_Items.append([Item_UPC,
                             Item_Description,
                             Item_Max_Qty,
                             Item_Order_Threshold,
                             Item_Replenishment_Order_Qty,
                             Item_On_Hand,
                             Item_Unit_Price])

    file_object.close()

    return Retail_Items

Retail_Items = Get_Retail_Item_Data()
print(type(Retail_Items))
print(len(Retail_Items))
print(Retail_Items)