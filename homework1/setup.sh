#!/bin/bash

# ============================================
# 作业1：Linux 练习脚本
# ============================================

# 1. 创建 linux_practice 文件夹及其子目录 docs 和 backup
mkdir -p linux_practice/docs linux_practice/backup

# 2. 在 docs 目录下创建三个文件
touch linux_practice/docs/readme.txt
touch linux_practice/docs/notes.log
touch linux_practice/docs/temp.tmp

# 3. 删除 temp.tmp，将 notes.log 重命名为 daily_report.txt
rm linux_practice/docs/temp.tmp
mv linux_practice/docs/notes.log linux_practice/docs/daily_report.txt

# 4. 向 daily_report.txt 写入第一行，追加第二行（当前日期）
echo "Project Status: Active" > linux_practice/docs/daily_report.txt
date >> linux_practice/docs/daily_report.txt

# 5. 将 docs 目录下的所有 .txt 文件复制到 backup 目录
cp linux_practice/docs/*.txt linux_practice/backup/

# 6. 将 backup 目录下所有文件权限修改为只读 (r--r--r-- = 444)
chmod 444 linux_practice/backup/*

# 7. 输出完成信息
for file in linux_practice/backup/*; do
    filename=$(basename "$file")
    echo "Archive Complete. File $filename is now read-only."
done
