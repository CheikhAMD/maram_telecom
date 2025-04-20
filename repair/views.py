# from django.shortcuts import render, redirect
# from .forms import RepairRequestForm

# def repair_form_view(request):
#     if request.method == 'POST':
#         form = RepairRequestForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('repair_success')
#     else:
#         form = RepairRequestForm()
#     return render(request, 'repair/repair_form.html', {'form': form})

# def repair_success_view(request):
#     return render(request, 'repair/repair_success.html')

from django.shortcuts import render, redirect
from .models import RepairRequest

def repair_form_view(request):
    if request.method == 'POST':
        # خذ القيم من POST
        user_name = request.POST.get('user_name')
        phone_model = request.POST.get('phone_model')
        issue_description = request.POST.get('issue_description')
        contact_info = request.POST.get('contact_info')
        # احفظ الطلب
        RepairRequest.objects.create(
            user_name=user_name,
            phone_model=phone_model,
            issue_description=issue_description,
            contact_info=contact_info
        )
        # ارسل المستخدم لصفحة النجاح
        return redirect('repair_success')
    return render(request, 'repair/repair_form.html')

def repair_success_view(request):
    return render(request, 'repair/repair_success.html')

