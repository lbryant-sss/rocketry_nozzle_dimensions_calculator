from django.shortcuts import render
from django.views import View
from math import sqrt, tan, radians, degrees, pi, exp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from django.conf import settings
from . models import PDF

#importing calculations
from .calculations import calculate_values

#import pdf Generator function
from .generator import generate_pdf
# Create your views here.

#F = P0 = ALT = OF = T0 = M = k = Lstar = P3 = Tt = v2 = mdot = mdot_fuel = mdot_oxidizer = Isp = Te = Mnum = At = Ae = Rt = Re = Ac = Rc = Lc = Ldn = Lcn = ER = None


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
        M = float(request.POST['molecular_mass'])
        k = float(request.POST['specific_heats_ratio'])
        Lstar = int(request.POST['chamber_length'])

        # Call the calculate_values function from calculations.py
        P3, PR, AR, ER, Tt, v2, mdot, mdot_fuel, mdot_oxidizer, Isp, Te, Mnum, At, Ae, Rt, Re, Ac, Rc, Lc, Ldn, Lcn = calculate_values(
            F, P0, ALT, OF, T0, M, k, Lstar
        )


        # Check if any of the calculated values are None
        

        '''
        Processing the context
        '''
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
            'throttle_temperature':Tt,
            #outputs
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

        generate_pdf(context)

        return render(request, self.template_name, context) 
            
        


        

