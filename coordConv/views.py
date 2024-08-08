from django.shortcuts import render

from .froms import utmForm, wgsForm

from pyproj import Transformer

# Create your views here.
def coordConv(request):
    title = "Coordinate Converter"

    if request.method == 'POST':
        print(request.POST)
        if request.POST['typeForm'] == "utm":

            print("masuk UTM")
            x = request.POST['x']
            y = request.POST['y']
            utm = request.POST['zone'] 
            
            # Perform the coordinate transformation
            transformer = Transformer.from_crs(utm, 'EPSG:4326', always_xy=True)
            long, lat = transformer.transform(x, y)
            # print(f"UTM Coordinates: {lat}, {long}")

            resultWGS ={
                'lattitude' : f"{lat:.8f}",
                'longitude' : f"{long:.8f}",
            }
            resultUTM = {
                'x' : x,   
                'y' : y,
                'utm' : utm,
            }

            utm_form = utmForm(resultUTM)
            wgs_form = wgsForm(resultWGS)

            # context['formUTM']= utmForm(resultUTM)
            # context['formWGS']= formWGS(resultWGS)

        elif request.POST['typeForm'] == "wgs":
            wgs_form = wgsForm(request.POST)
            print("masuk wgs")

            lattitude = request.POST.get('lattitude')
            longitude = request.POST.get('longitude')

            try:
                # Convert to float
                lattitude = float(lattitude)
                longitude = float(longitude)
                
                # Validate latitude and longitude
                if not (-90 <= lattitude <= 90):
                    raise ValueError(f"Invalid latitude value: {lattitude}")
                if not (-180 <= longitude <= 180):
                    raise ValueError(f"Invalid longitude value: {longitude}")

                # Calculate UTM zone number
                zone_number = int((longitude + 180) / 6) + 1
                
                # Handle both northern and southern hemisphere cases
                if lattitude >= 0:
                    utm_crs = f"epsg:326{zone_number:02d}"  # Northern Hemisphere
                else:
                    utm_crs = f"epsg:327{zone_number:02d}"  # Southern Hemisphere

                # Validate EPSG code
                try:
                    crs = CRS.from_string(utm_crs)
                except Exception as e:
                    raise ValueError(f"Invalid EPSG code: {utm_crs}. Error: {e}")

                # Create transformer and perform the transformation
                transformer = Transformer.from_crs("epsg:4326", utm_crs, always_xy=True)
                x, y = transformer.transform(longitude, lattitude)

                print(x, y)
                
                # Prepare result dictionaries
                resultWGS = {
                    'lattitude': lattitude,
                    'longitude': longitude,
                }
                resultUTM = {
                    'x': x,
                    'y': y,
                    'utm': utm_crs,
                }

                # Create forms with result data
                utm_form = utmForm(resultUTM)
                wgs_form = wgsForm(resultWGS)   
            except ValueError as ve:
                # Handle invalid input values
                print(f"ValueError: {ve}")
                # Optionally, add an error message to the form or context
            except Exception as e:
                # Handle other exceptions
                print(f"Error: {e}")
                # Optionally, add an error message to the form or context


    else:
        utm_form = utmForm()
        wgs_form = wgsForm()
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