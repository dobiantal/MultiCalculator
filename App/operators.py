#Összeadás művelete
def Addition(A:int, B:int):
    try:
        if (float(A)+float(B)) % (float(A)+float(B)).__round__(0) == 0:
            return int(float(A)+float(B))
        else:
            return float(A)+float(B)
    except ValueError:
        return "Értékhiba"
    except TypeError:
        return "Helytelen típus"
    except:
        return "Err"

#Osztás művelete
def div(OPERANDUS_A , OPERANDUS_B):
    try:
        return int(OPERANDUS_A) / int(OPERANDUS_B)
    except ValueError:
        return "Hibás érték!"
    except SyntaxError:
        return "Szintaktikai hiba!"
    except ZeroDivisionError:
        return "0-val való osztás 0-t ad!"

#Szorzás művelete
def multiplicate(OPERANDUS_A, OPERANDUS_B):
    if not (str(OPERANDUS_A).isnumeric() and str(OPERANDUS_B).isnumeric()):
        raise ValueError("Az OPERANDUS_A és OPERANDUS_B értékei csak számok lehetnek.")

    OPERANDUS_A = float(OPERANDUS_A)
    OPERANDUS_B = float(OPERANDUS_B)

    if OPERANDUS_A == 0 or OPERANDUS_B == 0:
        raise ValueError("Az OPERANDUS_A vagy OPERANDUS_B értéke nem lehet 0.")

    return OPERANDUS_A * OPERANDUS_B