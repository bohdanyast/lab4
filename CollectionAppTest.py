import CollectionApp as ca

u_collection = [int(i) for i in input("Введіть універсальну множину U: ").split(',') if i.strip()]
a_collection = [int(j) for j in input("Введіть множину A: ").split(',') if j.strip()]
b_collection = [int(k) for k in input("Введіть множину B: ").split(',') if k.strip()]

while True:
    a = input("\nВиберіть операцію(введіть цифрами):\n"
              "1.1 Об'єднання множин A i B\n"
              "1.2 Перетин множин A i B\n"
              "1.3 Різниця множин A i B\n"
              "1.4 Різниця множин B i A\n"
              "1.5 Доповнення множини A\n"
              "1.6 Доповнення множини В\n"
              "1.7 Симетрична різниця множин А і B\n"
              "1.8 Декартовий добуток множин A i B\n"
              "1.9 Декартовий добуток множин B i A\n"
              "--------------------------\n"
              "2.1 Чи є множина A підмножиною множини B\n"
              "2.2 Чи є множина В підмножиною множини А\n"
              "2.3 Чи є множини A i B рівними\n"
              "--------------------------\n"
              "3.1 Множина A у бітовий рядок\n"
              "3.2 Множина В у бітовий рядок\n"
              "--------------------------\n"
              "4 Операції з бітовими рядками(OR, XOR, NOT, AND)\n"
              "--------------------------\n"
              "5 Бітовий рядок в множину\n"
              )

    if float(a) == 1.1:
        print('A = ', set(a_collection))
        print('B = ', set(b_collection))
        print(f"Об'єднання: {set(ca.elems_in_a_or_b(a_collection, b_collection))}")
    elif float(a) == 1.2:
        print('A = ', set(a_collection))
        print('B = ', set(b_collection))
        print(f"Перетин: {set(ca.elems_in_a_and_b(a_collection, b_collection))}")
    elif float(a) == 1.3:
        print('A = ', set(a_collection))
        print('B = ', set(b_collection))
        print(f"Різниця множин A i B: {set(ca.elems_in_a_and_not_b(a_collection, b_collection))}")
    elif float(a) == 1.4:
        print('A = ', set(a_collection))
        print('B = ', set(b_collection))
        print(f"Різниця множин B i A: {set(ca.elems_in_a_and_not_b(b_collection, a_collection))}")
    elif float(a) == 1.5:
        print('U = ', set(u_collection))
        print('A = ', set(a_collection))
        print(f"Доповнення множини A: {set(ca.elems_in_u_not_in_a(u_collection, a_collection))}")
    elif float(a) == 1.6:
        print('U = ', set(u_collection))
        print('B = ', set(b_collection))
        print(f"Доповнення множини В: {set(ca.elems_in_u_not_in_a(u_collection, b_collection))}")
    elif float(a) == 1.7:
        print('A = ', set(a_collection))
        print('B = ', set(b_collection))
        print(f"Симетрична різниця множин А і B: {set(ca.elems_in_a_and_b_but_not_both(a_collection, b_collection))}")
    elif float(a) == 1.8:
        print('A = ', set(a_collection))
        print('B = ', set(b_collection))
        print('Декартовий добуток множин A i B:')
        ca.decart_multiplication_of_a_and_b(a_collection, b_collection)
    elif float(a) == 1.9:
        print('В = ', set(b_collection))
        print('А = ', set(a_collection))
        print('Декартовий добуток множин B i A:')
        ca.decart_multiplication_of_a_and_b(b_collection, a_collection)
    elif float(a) == 2.1:
        print('A = ', set(a_collection))
        print('B = ', set(b_collection))
        print(ca.is_subcollection(a_collection, b_collection))
    elif float(a) == 2.2:
        print('B = ', set(b_collection))
        print('A = ', set(a_collection))
        print(ca.is_subcollection(b_collection, a_collection))
    elif float(a) == 2.3:
        print('A = ', set(a_collection))
        print('B = ', set(b_collection))
        print(ca.are_collections_equal(a_collection, b_collection))
    elif float(a) == 3.1:
        print('U = ', set(u_collection))
        print('A = ', set(a_collection))
        print('Множина A у бітовий рядок:')
        print(ca.collection_into_bytes(u_collection, a_collection))
    elif float(a) == 3.2:
        print('U = ', set(u_collection))
        print('B = ', set(b_collection))
        print('Множина B у бітовий рядок:')
        print(ca.collection_into_bytes(u_collection, b_collection))
    elif float(a) == 4.0:
        print('A:', ca.collection_into_bytes(u_collection, a_collection))
        print('B:', ca.collection_into_bytes(u_collection, b_collection))
        operation = input('OR, XOR, AND, NOT: ')
        if operation == 'not':
            print(ca.operations_with_bytes_for_not(u_collection, a_collection, b_collection, input("A чи В: ")))
        else:
            print(ca.operations_with_bytes(u_collection, a_collection, b_collection, operation))

    elif float(a) == 5.0:
        operation = input('OR, XOR, AND, NOT: ').lower()
        if operation != 'not':
            print(ca.collection_into_bytes(u_collection, a_collection))
            print(operation)
            print(ca.collection_into_bytes(u_collection, b_collection))
            print(ca.operations_with_bytes(u_collection, a_collection, b_collection, operation))
            print(ca.transform_bytes_to_normal_collection(u_collection, a_collection, b_collection, operation))
            ca.print_and_compare_collections(u_collection, a_collection, b_collection, operation)
        if operation == 'not':
            ask_a_or_b_for_5 = input("A чи В: ")
            print(ca.transform_bytes_to_normal_collection(u_collection, a_collection, b_collection, 'not',
                                               ask_a_or_b_for_5))
            if ask_a_or_b_for_5.lower() == 'a':
                arr_to_compare1 = ca.elems_in_u_not_in_a(u_collection, a_collection)
                arr_to_compare2 = ca.transform_bytes_to_normal_collection(
                    u_collection, a_collection, b_collection, 'not', ask_a_or_b_for_5,
                    False
                )
                print(ca.are_collections_equal(arr_to_compare1, arr_to_compare2))
            elif ask_a_or_b_for_5.lower() == 'b':
                arr_to_compare1 = ca.elems_in_u_not_in_a(u_collection, b_collection)
                arr_to_compare2 = ca.transform_bytes_to_normal_collection(
                    u_collection, a_collection, b_collection, 'not', ask_a_or_b_for_5,
                    False
                )
                print(ca.are_collections_equal(arr_to_compare1, arr_to_compare2))
