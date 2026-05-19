# Homework 1 — Linux Practice

This repository contains my first homework assignment for practicing basic Linux shell operations.

## Contents

| File / Directory | Description |
|------------------|-------------|
| `setup.sh`       | Shell script that automates directory creation, file operations, renaming, copying, and permission changes |
| `linux_practice/`| Practice directory containing `docs/` and `backup/` subdirectories |
| `screenfetch.png`| Screenshot of the Linux environment |

## What `setup.sh` does

1. Creates the folder structure `linux_practice/docs` and `linux_practice/backup`
2. Creates three files under `docs/`: `readme.txt`, `notes.log`, `temp.tmp`
3. Removes `temp.tmp` and renames `notes.log` to `daily_report.txt`
4. Writes "Project Status: Active" and the current date into `daily_report.txt`
5. Copies all `.txt` files from `docs/` to `backup/`
6. Sets read-only permissions (`444`) on all files in `backup/`

## Author

- **GitHub**: [@ddl-cyber](https://github.com/ddl-cyber)
- **Email**: 202530462184@mail.scut.edu.cn
