import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from django.conf import settings
from .models import PDF  # Import your PDF model here
from datetime import datetime




def generate_pdf(data):
    #Generate the pdf without interracting with matplotlib gui
    plt.ioff()

    ff = data['thrust']
    chamber_p = data['chamber_pressure']
    height = data['altitude']
    fuel_r = data['fuel_ratio']
    chamber_t = data['chamber_temparature']
    molecular_m = data['molecular_mass']
    specific_h = data['specific_heats_ratio']
    chamber_l = data['chamber_length']
    throttle_t = data['throttle_temperature']
    impul = data['impulse']
    effective_e = data['effective_exhaust_velocity']
    mass_f = data['mass_flow_rate']
    oxidizer_mass_f = data['oxidizer_mass_flow_rate']
    fuel_m = data['fuel_mass_flow_rate']
    exit_t = data['exit_temparature']
    exit_m = data['exit_mach_number']
    pressure_r = data['pressure_ratio']
    expansion_r = data['expansion_ratio']
    throat_a = data['throat_area']
    exit_a = data['exit_area']
    throat_r = data['throat_radius']
    exit_r = data['exit_radius']
    chamber_r = data['chamber_radius']
    chamber_l = data['chamber_length']
    diverging_nozzle_l = data['diverging_nozzle_length']
    converging_nozzle_l = data['converging_nozzle_length']

    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = 'STIXGeneral'
    fig, ax = plt.subplots(figsize=(10, 14.5))

    name = 'Nozzle dimensions'
    inputs = 'Inputs You provided'
    thrust = 'thrust'
    cp = 'chamber_p'
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

    #Get the timestamp when the pdf is generated
    current_timestamp = datetime.now()
    formatted_time = current_timestamp.strftime("%d/%m/%y at %H:%M:%S")

   #Header
    plt.annotate(name, (0.02, 0.94), weight='bold', fontsize=20)
    plt.annotate(formatted_time, (0.02, 0.92), weight='regular', fontsize='10')
    #TO DO || Add user name
    #plt.annotate(maker,(0.02, 0.91), weight='regular', fontsize=10 )
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

    filename = 'Nozzle Dimensions.pdf'
    file_path = os.path.join(settings.MEDIA_ROOT, filename)

    with PdfPages(file_path) as pdf:
        pdf.savefig(fig, dpi=300, bbox_inches='tight')

    pdf_obj = PDF.objects.create(generate_pdf=file_path, file_path=file_path)
    pdf_obj.save()


    return pdf_obj
    

