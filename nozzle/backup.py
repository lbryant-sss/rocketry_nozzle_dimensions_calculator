from django.shortcuts import render
from django.views import View
from math import sqrt, tan, radians, degrees, pi, exp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from django.conf import settings
from . models import PDF
# Create your views here.

#F = P0 = ALT = OF = T0 = M = k = Lstar = P3 = Tt = v2 = mdot = mdot_fuel = mdot_oxidizer = Isp = Te = Mnum = At = Ae = Rt = Re = Ac = Rc = Lc = Ldn = Lcn = ER = None


class home(View):
    template_name = 'pages/home.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


    def post(self, request, *args, **kwargs):
        
        global F, P0, ALT, OF, T0, M, k, Lstar, P3, Tt, v2, mdot, mdot_fuel, mdot_oxidizer, Isp, Te, Mnum, At, Ae, Rt, Re, Ac, Rc, Lc, Ldn, Lcn, ER
        
        try:  # Attempt to calculate values
            
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

            
        except (ValueError, ZeroDivisionError):  # Exception thrown
            print("\n", "Error while attempting to solve. Please enter a valid value"
                " for every parameter.")



        #Create pdf data
            #inputs
            ff = F
            chamber_p = P0
            height = ALT
            fuel_r = OF
            chamber_t = T0
            molecular_m = M
            specific_h = k
            chamber_l = Lstar
            throttle_t = Tt#outputs
            impul = Isp
            effective_e = v2
            mass_f = mdot
            oxidizer_mass_f = mdot_oxidizer
            fuel_m = mdot_fuel
            exit_t = Te
            exit_m = Mnum
            pressure_r = PR
            expansion_r = ER
            #Nozzle dimensions
            throat_a = At
            exit_a = Ae
            throat_r = Rt
            exit_r = Re
            chamber_r = R,
            chamber_l = Lc
            diverging_nozzle_l = Ldn
            converging_nozzle_l = Lcn
        # Setting style for bar graphs
        # set font
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['font.sans-serif'] = 'STIXGeneral'
        fig, ax = plt.subplots(figsize=(10, 14.5))
        # remove axes
        #plt.axis('off')
        name = 'Nozzle dimensions'
        inputs = 'Inputs You provided'
        thrust = 'thrust'
        cp = 'chamber_pressure'
        alt = 'altitude'
        fuel = 'fuel_ratio'
        cp = 'chamber_temparature'
        mass = 'molecular_mass'
        shr = 'specific_heats_ratio'
        cl = 'chamber_length'
        tt = 'throttle_temperature'
        ev = 'Effective_exhaust_velocity :'

        outputs = 'Relevant Outputs'
        imp = 'impulse'
        eev = 'effective_exhaust_velocity'
        flow_rate = 'mass_flow_rate'
        oxmfr = 'oxidizer_mass_flow_rate'
        fmfr = 'fuel_mass_flow_rate'
        et = 'exit_temparature'
        mach = 'exit_mach_number'
        pa = 'pressure_ratio'
        er = 'expansion_ratio'

        ta = 'throat_area'
        ea = 'exit_area'
        tr = 'throat_radius'
        erad = 'exit_radius'
        cr = 'chamber_radius'
        cl = 'chamber_length'
        dnl = 'diverging_nozzle_length'
        cnl = 'converging_nozzle_length'
        dime = 'Calculated Nozzle Dimensions'
        #Header
        plt.annotate(name, (0.02, 0.94), weight='bold', fontsize=20)
        plt.annotate(inputs, (0.02, 0.88), weight='bold', fontsize=20)
        #Input Identifiers
        plt.annotate(thrust, (0.05, 0.84), weight='regular', fontsize=12)
        plt.annotate(cp, (0.05, 0.82), weight='regular', fontsize=12)
        plt.annotate(alt, (0.05, 0.8), weight='regular', fontsize=12)
        plt.annotate(fuel, (0.05, 0.78), weight='regular', fontsize=12)
        plt.annotate(cp, (0.05, 0.76), weight='regular', fontsize=12)
        plt.annotate(mass, (0.05, 0.74), weight='regular', fontsize=12)
        plt.annotate(shr, (0.05, 0.72), weight='regular', fontsize=12)
        plt.annotate(cl, (0.05, 0.7), weight='regular', fontsize=12)
        plt.annotate(tt, (0.05, 0.68), weight='regular', fontsize=12)
        plt.annotate(ev, (0.05, 0.66), weight='regular', fontsize=12)
        #Input values
        plt.annotate(ff, (0.5, 0.84), weight='regular', fontsize=12)
        plt.annotate(chamber_p, (0.5, 0.82), weight='regular', fontsize=12)
        plt.annotate(height, (0.5, 0.8), weight='regular', fontsize=12)
        plt.annotate(fuel, (0.5, 0.78), weight='regular', fontsize=12)
        plt.annotate(fuel_r, (0.5, 0.76), weight='regular', fontsize=12)
        plt.annotate(chamber_t, (0.5, 0.74), weight='regular', fontsize=12)
        plt.annotate(molecular_m, (0.5, 0.72), weight='regular', fontsize=12)
        plt.annotate(specific_h, (0.5, 0.7), weight='regular', fontsize=12)
        plt.annotate(chamber_l, (0.5, 0.68), weight='regular', fontsize=12)
        plt.annotate(throttle_t, (0.5, 0.66), weight='regular', fontsize=12)
        #outputs

        plt.annotate(outputs, (.02, 0.62), weight='bold', fontsize=20)
        #Identifiers (Variables)
        plt.annotate(imp, (0.05, 0.58), weight='regular', fontsize=12)
        plt.annotate(eev, (0.05, 0.56), weight='regular', fontsize=12)
        plt.annotate(flow_rate, (0.05, 0.54), weight='regular', fontsize=12)
        plt.annotate(oxmfr, (0.05, 0.52), weight='regular', fontsize=12)
        plt.annotate(fmfr, (0.05, 0.5), weight='regular', fontsize=12)
        plt.annotate(et, (0.05, 0.48), weight='regular', fontsize=12)
        plt.annotate(mach, (0.05, 0.46), weight='regular', fontsize=12)
        plt.annotate(pa, (0.05, 0.44), weight='regular', fontsize=12)
        plt.annotate(er, (0.05, 0.42), weight='regular', fontsize=12)
        #Values of output
        plt.annotate(impul, (0.5, 0.58), weight='regular', fontsize=12)
        plt.annotate(effective_e, (0.5, 0.56), weight='regular', fontsize=12)
        plt.annotate(mass_f, (0.5, 0.54), weight='regular', fontsize=12)
        plt.annotate(oxidizer_mass_f, (0.5, 0.52), weight='regular', fontsize=12)
        plt.annotate(fuel_m, (0.5, 0.5), weight='regular', fontsize=12)
        plt.annotate(exit_t, (0.5, 0.48), weight='regular', fontsize=12)
        plt.annotate(exit_m, (0.5, 0.46), weight='regular', fontsize=12)
        plt.annotate(pressure_r, (0.5, 0.44), weight='regular', fontsize=12)
        plt.annotate(expansion_r, (0.5, 0.42), weight='regular', fontsize=12)

        #Approx. Calculated Nozzle Dimensions

        plt.annotate(dime, (.02,0.38), weight='bold', fontsize=20)
        #Dimensions variables
        plt.annotate(ta, (0.05, 0.34), weight='regular', fontsize=12)
        plt.annotate(ea, (0.05, 0.32), weight='regular', fontsize=12)
        plt.annotate(tr, (0.05, 0.3), weight='regular', fontsize=12)
        plt.annotate(erad, (0.05, 0.28), weight='regular', fontsize=12)
        plt.annotate(cr, (0.05, 0.26), weight='regular', fontsize=12)
        plt.annotate(cl, (0.05, 0.24), weight='regular', fontsize=12)
        plt.annotate(dnl, (0.05, 0.22), weight='regular', fontsize=12)
        plt.annotate(cnl, (0.05, 0.2), weight='regular', fontsize=12)
        #Dime Values
        plt.annotate(throat_a, (0.5, 0.34), weight='regular', fontsize=12)
        plt.annotate(exit_a, (0.5, 0.32), weight='regular', fontsize=12)
        plt.annotate(throat_r, (0.5, 0.3), weight='regular', fontsize=12)
        plt.annotate(exit_r, (0.5, 0.28), weight='regular', fontsize=12)
        plt.annotate(chamber_r, (0.5, 0.26), weight='regular', fontsize=12)
        plt.annotate(chamber_l, (0.5, 0.24), weight='regular', fontsize=12)
        plt.annotate(diverging_nozzle_l, (0.5, 0.22), weight='regular', fontsize=12)
        plt.annotate(converging_nozzle_l, (0.5, 0.2), weight='regular', fontsize=12)
        plt.axis('off')

        #Setting the path..
        filename = 'Nozzle Dimensions.pdf'
        file_path = '%s%s' % (settings.MEDIA_ROOT, filename)
        plt.savefig(file_path, dpi=300, bbox_inches='tight')


        #Adding the generated file to db
        x = PDF.objects.create()
        x.save()











        return render(request, self.template_name, context)

