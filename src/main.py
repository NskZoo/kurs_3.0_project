from func import load_operations, sort_by_ex, sort_by_date, format_card, format_date, format_accaunt


def main():
    operations = load_operations()
    sorted_executed = sort_by_ex(operations)
    sorted_date = sort_by_date(sorted_executed)

    five_operations = sorted_date[0:5]

    for operation in five_operations:
        date = format_date(operation["date"])
        details_list = []
        to_field = operation["to"]
        from_field = operation.get("from")
        details_list.append(from_field)
        details_list.append(to_field)
        mask_details = []

        for field in details_list:
            if field is None:
                mask_details.append("")
            else:
                field_split = field.split(" ")
                if "Счет" in field_split:
                    mask_number = format_accaunt(field_split[-1])
                else:
                    mask_number = format_card(field_split[-1])
                mask_field = " ".join(field_split[:-1]) + " " + mask_number
                mask_details.append(mask_field)


        print(f"""{date} {operation["description"]} 
{mask_details[0]} -> {mask_details[1]} 
{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]} 
""")



if __name__ == "__main__":
    main()



