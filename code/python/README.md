# Python

In biology and other scientific research:

- For statistics, we tend to use `R`
- For machine learning, we use `Python`

## Convert ipython notebook to PDF or HTML

```bash
jupyter nbconvert --execute --to pdf {filename}.ipynb
```

`--execute` means including the notebook output

prerequisite:

1. `notebook`, not `ipykernel`
2. `pandoc` , for Debian `sudo apt install pandoc`
3. `latex converter`, for Debian `sudo apt install texlive-xetex`