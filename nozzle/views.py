from django.shortcuts import render
from django.views import View
from math import sqrt, tan, radians, degrees, pi, exp
# Create your views here.

class home(View):
    template_name = 'pages/home.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


    def post(self, request, *args, **kwargs):
        global F, P0, ALT, OF, T0, M, k, Lstar
        #DATA INPUT
        F = int(request.POST['thrust'])
        P0 = int(request.POST['chamber_pressure'])
        ALT = int(request.POST['altitude'])
        OF = int(request.POST['fuel_ratio'])
        T0 = int(request.POST['chamber_temparature'])
        M = int(request.POST['molecular_mass'])
        k = int(request.POST['specific_heats_ratio'])
        Lstar = int(request.POST['chamber_length'])

        #CALCULATIONS
        '''
        Setting the base conditions
        '''
        global P3
        h = ALT
        if (h >= 25000):  # Upper Stratosphere
            T = -131.21 + 0.00299 * h
            P3 = (2.488 * ((T + 273.1) / 216.6) ** (-11.388))*1000
        elif (11000 < h < 25000):  # Lower Stratosphere
            T = -56.46
            P3 = (22.65 * exp(1.73 - 0.000157 * h))*1000
        else: # Troposphere
            T = 15.04 - 0.00649 * h
            P3 = (101.29 * ((T + 273.1) / 288.08) ** (5.256))*1000
        """
        Attempts to calculate and print values.
        """
        try:  # Attempt to calculate values
            R = (8314.3 / M)
            PR = (P3 / P0)
            AR = (((k + 1) / 2) ** (1 / (k - 1))) * ((P3 / P0) ** (1 / k)) * (sqrt(((k + 1) / (k - 1)) * (1 - ((P3 / P0) ** ((k - 1) / k)))))
            #AR = (((k + 1) / 2) ** (1 / (k - 1))) * ((P3 / P0) ** (1 / k)) * (sqrt(((k + 1) / (k - 1)) * (1 - ((P3 / P0) ** ((k - 1) / k)))))
            ER = 1 / AR
            Tt = (2 * T0) / (k + 1)
            v2 = sqrt((2 * k / (k - 1)) * ((R) * T0) * (1 - ((P3 / P0) ** ((k - 1) / k))))
            mdot = F / v2
            mdot_fuel = (mdot / (OF + 1))
            mdot_oxidizer = (mdot / (OF + 1)) * OF
            Isp = F / (mdot * 9.80655)
            Te = T0 / ((P0 / P3) ** ((k - 1) / k))
            Mnum = (v2 / (sqrt(k * (R) * (Te))))
            At = ((mdot) * (sqrt((k * R * T0)))) / (k * P0 * (sqrt(((2 / (k + 1)) ** ((k + 1) / (k - 1))))))
            Ae = ER * At
            Rt = sqrt(At / pi)
            Re = sqrt(Ae / pi)
            Ac = At * 8
            Rc = sqrt((Ac) / pi)
            Lc = ((At) * Lstar) / (Ac)
            Ldn = ((Re) - (Rt)) / (tan(radians(15)))
            Lcn = ((Rc) - (Rt)) / (tan(radians(45)))
        except (ValueError, ZeroDivisionError):  # Exception thrown
            print("\n", "Error while attempting to solve. Please enter a valid value"
                " for every parameter.")


            '''
            Processing the context
            '''
            #global context
        context = {
            #inputs
            'thrust':F,
            'chamber_pressure':P0,
            'altitude':ALT,
            'fuel_ratio':OF,
            'chamber_temparature':T0,
            'molecular_mass':M,
            'specific_heats_ratio':k,
            'chamber_length':Lstar,
            'throttle_temperature':Tt,#outputs
            'impulse':Isp,
            'effective_exhaust_velocity':v2,
            'mass_flow_rate':mdot,
            'oxidizer_mass_flow_rate':mdot_oxidizer,
            'fuel_mass_flow_rate':mdot_fuel,
            'exit_temparature':Te,
            'exit_mach_number':Mnum,
            'pressure_ratio':PR,
            'expansion_ratio':ER,
            #Nozzle dimensions
            'throat_area':At,
            'exit_area':Ae,
            'throat_radius':Rt,
            'exit_radius':Re,
            'chamber_radius':Rc,
            'chamber_length':Lc,
            'diverging_nozzle_length':Ldn,
            'converging_nozzle_length':Lcn,
        }


        return render(request, self.template_name, context)

