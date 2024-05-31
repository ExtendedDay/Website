@echo off
for %%f in (*.png) do cwebp -q 90 -alpha_q 100 "%%f" -o "%%~nf.webp"
