# об'єднання множин
def elems_in_a_or_b(a_coll, b_coll):
    either_a_b = []

    for elem in a_coll:
        either_a_b.append(elem)

    for elem in b_coll:
        if elem not in either_a_b:
            either_a_b.append(elem)

    return either_a_b


# перетин множин
def elems_in_a_and_b(a_coll, b_coll):
    both_a_b = []

    for elem in a_coll:
        if elem in b_coll and elem not in both_a_b:
            both_a_b.append(elem)

    return both_a_b


# різниця множин
def elems_in_a_and_not_b(a_coll, b_coll):
    a_not_b = []

    for elem in a_coll:
        if elem not in b_coll and elem not in a_not_b:
            a_not_b.append(elem)

    return a_not_b


# множинне доповнення
def elems_in_u_not_in_a(u_coll, a_coll):
    in_u_not_in_a = []

    for elem in u_coll:
        if elem not in a_coll and elem not in in_u_not_in_a:
            in_u_not_in_a.append(elem)

    return in_u_not_in_a


# симетричне різниця
def elems_in_a_and_b_but_not_both(a_coll, b_coll):
    only_in_a = elems_in_a_and_not_b(a_coll, b_coll)
    only_in_b = elems_in_a_and_not_b(b_coll, a_coll)
    in_a_and_b_but_not_both = only_in_a + only_in_b

    return in_a_and_b_but_not_both


# декартовий добуток
def decart_multiplication_of_a_and_b(a_coll, b_coll):
    decart_multiplication = []
    if len(a_coll) == 0 or len(b_coll) == 0:
        decart_multiplication = []
        print(decart_multiplication)
    else:
        for i in range(len(a_coll)):
            for j in range(len(b_coll)):
                decart_multiplication.append([a_coll[i], b_coll[j]])

        rows = len(b_coll)
        i = 0

        for arr in decart_multiplication:
            i += 1
            print(arr, end=' ')
            if i % rows == 0:
                print()


# чи є підмножиною
def is_subcollection(a_coll, b_coll):
    flag = False
    for elem in a_coll:
        if elem in b_coll:
            flag = True
        else:
            flag = False
            break

    if len(a_coll) == 0:
        flag = True

    if flag:
        return f"Множина {set(a_coll)} є підмножиною {set(b_coll)}"
    else:
        return f"Множина {set(a_coll)} не є підмножиною {set(b_coll)}"


# чи є рівними множини
def are_collections_equal(a_coll, b_coll):
    flag = False
    for elem in a_coll:
        if elem in b_coll:
            flag = True
        else:
            flag = False
            break

    if len(a_coll) == len(b_coll) == 0:
        flag = True

    if flag:
        return f"{set(a_coll)} = {set(b_coll)}"
    else:
        return f"{set(a_coll)} != {set(b_coll)}"


# в байти
def collection_into_bytes(u_coll, a_coll):
    byte = ''
    for elem in u_coll:
        if elem in a_coll:
            byte += '1'
        else:
            byte += '0'
    return byte


def operations_with_bytes_for_not(u_coll, a_coll, b_coll, collection):
    total = ''
    bytes_in_a = collection_into_bytes(u_coll, a_coll)
    bytes_in_b = collection_into_bytes(u_coll, b_coll)
    if collection == 'a':
        for i in range(len(bytes_in_a)):
            total += str(int(not int(bytes_in_a[i])))
    elif collection == 'b':
        for j in range(len(bytes_in_b)):
            total += str(int(not int(bytes_in_b[j])))

    return total


# операції на байтами
def operations_with_bytes(u_coll, a_coll, b_coll, operation):
    bytes_in_a = collection_into_bytes(u_coll, a_coll)
    bytes_in_b = collection_into_bytes(u_coll, b_coll)
    total = ''
    operation = operation.lower().replace(' ', '')

    if operation == 'or':
        for i in range(len(bytes_in_a)):
            total += str(int(bytes_in_a[i]) or int(bytes_in_b[i]))
    elif operation == 'and':
        for i in range(len(bytes_in_a)):
            total += str(int(bytes_in_a[i]) and int(bytes_in_b[i]))
    elif operation == 'xor':
        for i in range(len(bytes_in_a)):
            total += str(int(bytes_in_a[i]) ^ int(bytes_in_b[i]))
    else:
        print("Unsupported operation")

    return total


# із байтів в множину
def transform_bytes_to_normal_collection(u_coll, a_coll, b_coll, operation, collection='', debug=True):
    total_a_collection = []
    coll = a_coll if collection.lower() == 'a' else b_coll
    if operation == 'not':
        if debug:
            print(f"U: {set(u_coll)}")
            print(f"{collection.upper()}: {set(coll)}")
            print('-----------------')
            print(f"{collection.upper()}: {collection_into_bytes(u_coll, coll)}")
            print(f"NOT {collection.upper()}: {collection_into_bytes(u_coll, elems_in_u_not_in_a(u_coll, coll))}")

        result_bytes = operations_with_bytes_for_not(u_coll, a_coll, b_coll, collection)
        for i in range(len(result_bytes)):
            if result_bytes[i] == '1':
                total_a_collection.append(u_coll[i])
    else:
        if debug:
            print('A: ', set(a_coll))
            print('B: ', set(b_coll))
        result_bytes = operations_with_bytes(u_coll, a_coll, b_coll, operation)
        for i in range(len(result_bytes)):
            if result_bytes[i] == '1':
                total_a_collection.append(u_coll[i])

    return set(total_a_collection)


def print_and_compare_collections(u_coll, a_coll, b_coll, operation):
    if operation == 'or':
        or_coll_original = elems_in_a_or_b(a_coll, b_coll)
        or_call_from_bytes = transform_bytes_to_normal_collection(
            u_coll, a_coll, b_coll, 'or','', False
        )
        print(are_collections_equal(or_coll_original, or_call_from_bytes))
    if operation == 'and':
        and_coll_original = elems_in_a_and_b(a_coll, b_coll)
        and_call_from_bytes = transform_bytes_to_normal_collection(
            u_coll, a_coll, b_coll, 'and', '', False
        )
        print(are_collections_equal(and_coll_original, and_call_from_bytes))
    if operation == 'xor':
        xor_coll_original = elems_in_a_and_b_but_not_both(a_coll, b_coll)
        xor_call_from_bytes = transform_bytes_to_normal_collection(
            u_coll, a_coll, b_coll, 'xor', '', False
        )
        print(are_collections_equal(xor_coll_original, xor_call_from_bytes))