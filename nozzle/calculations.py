from math import sqrt, tan, radians, degrees, pi, exp

from math import sqrt, exp, tan, radians, pi

global P3, Tt, v2, mdot, mdot_fuel, mdot_oxidizer, Isp, Te, Mnum, At, Ae, Rt, Re, Ac, Rc, Lc, Ldn, Lcn, ER
        
    

def calculate_values(F, P0, ALT, OF, T0, M, k, Lstar):
    try:
        # Calculate P3
        h = ALT
        if h >= 25000:  # Upper Stratosphere
            T = -131.21 + 0.00299 * h
            P3 = (2.488 * ((T + 273.1) / 216.6) ** (-11.388)) * 1000
        elif 11000 < h < 25000:  # Lower Stratosphere
            T = -56.46
            P3 = (22.65 * exp(1.73 - 0.000157 * h)) * 1000
        else:  # Troposphere
            T = 15.04 - 0.00649 * h
            P3 = (101.29 * ((T + 273.1) / 288.08) ** (5.256)) * 1000

        # Perform other calculations
        R = (8314.3 / M)
        PR = (P3 / P0)
        AR = (((k + 1) / 2) ** (1 / (k - 1))) * ((P3 / P0) ** (1 / k)) * (
            sqrt(((k + 1) / (k - 1)) * (1 - ((P3 / P0) ** ((k - 1) / k))))
        )
        ER = 1 / AR
        Tt = (2 * T0) / (k + 1)
        v2 = sqrt(
            (2 * k / (k - 1)) * ((R) * T0) * (1 - ((P3 / P0) ** ((k - 1) / k)))
        )
        mdot = F / v2
        mdot_fuel = mdot / (OF + 1)
        mdot_oxidizer = (mdot / (OF + 1)) * OF
        Isp = F / (mdot * 9.80655)
        Te = T0 / ((P0 / P3) ** ((k - 1) / k))
        Mnum = v2 / (sqrt(k * (R) * (Te)))
        At = (
            (mdot)
            * (sqrt((k * R * T0)))
        ) / (k * P0 * (sqrt(((2 / (k + 1)) ** ((k + 1) / (k - 1))))))
        Ae = ER * At
        Rt = sqrt(At / pi)
        Re = sqrt(Ae / pi)
        Ac = At * 8
        Rc = sqrt((Ac) / pi)
        Lc = ((At) * Lstar) / (Ac)
        Ldn = ((Re) - (Rt)) / (tan(radians(15)))
        Lcn = ((Rc) - (Rt)) / (tan(radians(45)))

        # Return the calculated values
        return (
            P3,
            PR,
            AR,
            ER,
            Tt,
            v2,
            mdot,
            mdot_fuel,
            mdot_oxidizer,
            Isp,
            Te,
            Mnum,
            At,
            Ae,
            Rt,
            Re,
            Ac,
            Rc,
            Lc,
            Ldn,
            Lcn,
        )
    except (ValueError, ZeroDivisionError):
        # If any errors occur during calculation, return None for all values
        return (None,) * 21
