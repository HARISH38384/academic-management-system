@echo off
echo Initializing Git...
git init

echo Adding files...
git add .

echo Configuring Git User...
git config user.name "Harish"
git config user.email "harish@example.com"

echo Committing...
git commit -m "Finalizing Academic Management System with Modern UI and Animations"

echo Setting branch to main...
git branch -M main

echo Adding remote repository...
git remote remove origin 2>nul
git remote add origin https://github.com/HARISH38384/academic-management-system.git

echo Pushing to GitHub (Forcefully integrating)...
git push -u origin main -f

echo.
echo ========================================
echo Done! Please check your GitHub repository.
echo ========================================
pause
