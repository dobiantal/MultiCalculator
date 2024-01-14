import math
from decimal import Decimal, getcontext

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


#négyzetgyök elkészítése
def negyzetgyok(OPERANDUS_A):

    """
    if (type(OPERANDUS_A) == str):
        return 0
    """

    try:
        OPERANDUS_A = float(OPERANDUS_A)
        # Ha negatív számot kap 0 val tér vissza
        if (OPERANDUS_A < 0):
            return 0

        return math.sqrt(OPERANDUS_A)
    except TypeError:
        return "TERR"
    except:
        return "ERR"

#kivonás művelete
def subtract(OPERANDUS_A, OPERANDUS_B):
    # Beállítja a kívánt pontosságot (8 tizedesjegy)
    getcontext().prec = 10

    try:
        eredmeny = Decimal(OPERANDUS_A) - Decimal(OPERANDUS_B)
        return round(eredmeny, 8)
    except Exception as e:
        print("Hiba történt a kivonás során:", e)
        return None  # Jelzés hogy a művelet nem sikerült