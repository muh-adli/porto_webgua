from django.shortcuts import render

from .froms import utmForm, wgsForm

# Create your views here.
def coordConv(request):
    title = "Coordinate Converter"

    if request.method == 'POST':
        print(request.POST)
        if 'utm_submit' in request.POST:
            utm_form = utmForm(request.POST)
            print("masuk utm")
            print(utm_form)
            # wgs_form = wgsForm()  # Create an empty WGSForm
            # if utm_form.is_valid():
            #     # Process UTM form data
            #     x = utm_form.cleaned_data['x']
            #     y = utm_form.cleaned_data['y']
            #     utm = utm_form.cleaned_data['utm']
            #     # Perform necessary actions with the UTM form data
            #     # Redirect or render a success page
            #     return redirect('success_url')  # Replace with your success URL

        elif 'wgs_submit' in request.POST:
            wgs_form = wgsForm(request.POST)
            print("masuk wgs")
            print(wgs_form)
            # utm_form = utmForm()  # Create an empty UTMForm
            # if wgs_form.is_valid():
            #     # Process WGS form data
            #     latitude = wgs_form.cleaned_data['lattitude']
            #     longitude = wgs_form.cleaned_data['longitude']
            #     # Perform necessary actions with the WGS form data
            #     # Redirect or render a success page
            #     return redirect('success_url')

    else:
        utm_form = utmForm(prefix='utm')
        wgs_form = wgsForm(prefix='wgs')
        context = {
            'title': title,
            'utm_form': utm_form,
            'wgs_form': wgs_form,
        }

        return render(request, 'coordconv/coordConv.html', context)

def coordExport(request):
    title = "Export - Coordinate Converter"

    context = {
        'title': title,
    }
    return render(request, 'coordconv/coordConv.html', context)