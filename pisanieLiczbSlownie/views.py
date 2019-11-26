from django.shortcuts import render
import pisanieLiczbSlownie.convert_numbers as cn


def convert_number(request):
    converted_number = ""
    if request.GET.get('convert_button'):

        converted_number = cn.convert_number_to_written_in_words(int(request.GET.get('input_number')))

    return render(request, 'pisanieLiczbSlownie/convert_number.html', {'converted_number': converted_number})
