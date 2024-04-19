import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from django.conf import settings
from .models import PDF  # Import your PDF model here

def generate_pdf(data):
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

    plt.annotate(name, (0.02, 0.94), weight='bold', fontsize=20)
    plt.annotate(inputs, (0.02, 0.88), weight='bold', fontsize=20)
    plt.annotate(thrust, (0.05, 0.84), weight='regular', fontsize=12)
    # Add other input identifiers and values here...
    plt.annotate(ff, (0.5, 0.84), weight='regular', fontsize=12)
    # Add other input values here...

    plt.annotate(outputs, (.02, 0.62), weight='bold', fontsize=20)
    # Add output identifiers and values here...

    plt.annotate(dime, (.02, 0.38), weight='bold', fontsize=20)
    # Add nozzle dimension identifiers and values here...

    plt.axis('off')

    filename = 'Nozzle Dimensions.pdf'
    file_path = '%s%s' % (settings.MEDIA_ROOT, filename)

    with PdfPages(file_path) as pdf:
        pdf.savefig(fig, dpi=300, bbox_inches='tight')

    x = PDF.objects.create()
    x.save()
