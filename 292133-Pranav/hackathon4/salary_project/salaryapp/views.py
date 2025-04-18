from django.shortcuts import render

# to display the salary form
def salary_form(request):
    # render the salary input
    return render(request, r'D:\Python Training\Python_Training\292133-Pranav\hackathon4\salary_project\salaryapp\templates\salary_form.html')

# to process the form data and calculate the net salary
def salary_result(request):
    if request.method == 'POST':
        name = request.POST['name']
        gross_salary = float(request.POST['gross_salary'])
        tax = float(request.POST['tax'])
        bonus = float(request.POST['bonus'])

        net_salary = gross_salary - (gross_salary * tax / 100) + (gross_salary * bonus / 100)

        # sends the result to the result page
        return render(request, r'D:\Python Training\Python_Training\292133-Pranav\hackathon4\salary_project\salaryapp\templates\salary_result.html', {
            'name': name,
            'net_salary': net_salary
        })
# to handle jumbled word
def jumble_word(request):
    jumbled = ""
    word = ""
    if request.method == 'POST':
        import random
        word = request.POST['word']
        jumbled = ''.join(random.sample(word, len(word)))
    return render(request, r'D:\Python Training\Python_Training\292133-Pranav\hackathon4\salary_project\salaryapp\templates\jumble_word.html', {
        'original': word,
        'jumbled': jumbled
    })
