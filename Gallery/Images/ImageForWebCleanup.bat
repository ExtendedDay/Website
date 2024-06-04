@echo off
setlocal enabledelayedexpansion

:: Convert.png and.jpg to.webp
for %%f in (*.png *.jpg) do (
    cwebp -q 90 -alpha_q 100 "%%f" -o "%%~nf.webp"
)

:: Check if conversion was successful and delete original files
for %%f in (*.png *.jpg) do (
    if exist "%%~nf.webp" (
        del "%%f"
    )
)

endlocal
