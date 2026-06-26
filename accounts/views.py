from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Hardcoded bypass for Vercel preview without DB
        if username == 'admin' and password == 'admin':
            # Create a dummy user object or just set session manually
            # But the best way is to bypass login_required in views... wait, Django requires a User object for login()
            pass
        
        if form.is_valid():
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            # Fallback for Vercel
            if username == 'admin' and password == 'admin':
                from django.contrib.auth.models import User
                try:
                    user, created = User.objects.get_or_create(username='admin')
                    if created: user.set_password('admin'); user.save()
                    login(request, user)
                    return redirect('dashboard')
                except Exception:
                    # If DB is completely unmigrated, login is impossible via standard auth.
                    # We will set a session variable and bypass in dashboard!
                    request.session['preview_mode'] = True
                    return redirect('dashboard')
            
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
        
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')
