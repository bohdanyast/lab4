# NUMBER 1. Check properties of the relation:

# reflexivity
def is_reflexive(matrix):
    for i in range(len(matrix)):
        if not matrix[i][i]:
            return False

    return True


def is_antireflexive(matrix):
    for i in range(len(matrix)):
        if matrix[i][i]:
            return False

    return True


def is_not_reflexive(matrix):
    if not is_reflexive(matrix) and not is_antireflexive(matrix):
        return True

    return False


def get_reflexivity(matrix):  # reflexivity text
    reflexivity = ''

    if is_reflexive(matrix):
        reflexivity = 'рефлексивне'
    elif is_antireflexive(matrix):
        reflexivity = 'антирефлексивне'
    elif is_not_reflexive(matrix):
        reflexivity = 'нерефлексивне'

    return reflexivity


# symmetry

def is_symmetrical(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] and not matrix[j][i]:
                return False

    return True


def is_asymmetrical(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] and matrix[j][i]:
                return False

    return True


def is_antisymmetrical(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i != j and matrix[i][j] and matrix[j][i]:
                return False

    return True


def is_not_symmetrical(matrix):
    if not is_symmetrical(matrix) and not is_antisymmetrical(matrix) and not is_asymmetrical(matrix):
        return True

    return False


def get_symmetry(matrix):  # symmetry text
    symmetry = ''

    if is_symmetrical(matrix):
        symmetry = 'симетричне'
    elif is_asymmetrical(matrix):
        symmetry = 'асиметричне'
    elif is_antisymmetrical(matrix):
        symmetry = 'антисиметричне'
    elif is_not_symmetrical(matrix):
        symmetry = 'несиметричне'

    return symmetry


# transitivity

def is_transitive(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j]:
                for k in range(len(matrix)):
                    if matrix[j][k] and not matrix[i][k]:
                        return False

    return True


def is_antitransitive(matrix):
    if not is_transitive(matrix):
        return True

    return False


def get_transitivity(matrix):  # transitivity text
    transitivity = ''

    if is_transitive(matrix):
        transitivity = 'транзитивне'
    elif is_antitransitive(matrix):
        transitivity = 'антитранзитивне'

    return transitivity


# NUMBER 2. Check relation of the relation:

def is_relation_of_equation(matrix):
    return is_reflexive(matrix) and is_transitive(matrix) and is_symmetrical(matrix)


def is_relation_of_partial_sequence(matrix):
    return is_reflexive(matrix) and is_transitive(matrix) and is_antisymmetrical(matrix)


def is_relation_of_strict_sequence(matrix):
    return is_antireflexive(matrix) and is_transitive(matrix) and is_asymmetrical(matrix)


# NUMBER 3. Closure of non-existing properties:

def get_reflexive_closure(matrix):
    matrix_const = matrix
    for i in range(len(matrix_const)):
        matrix_const[i][i] = 1

    return matrix_const


def get_symmetrical_closure(matrix):
    matrix_const = matrix
    for i in range(len(matrix_const)):
        for j in range(len(matrix_const)):
            if matrix_const[i][j]:
                matrix_const[j][i] = 1

    return matrix_const


def get_transitive_closure(matrix):
    matrix_const = matrix
    for i in range(len(matrix_const)):
        for j in range(len(matrix_const)):
            if matrix_const[i][j]:
                for k in range(len(matrix_const)):
                    if matrix_const[j][k] and not matrix_const[i][k]:
                        matrix_const[i][k] = 1

    return matrix_const