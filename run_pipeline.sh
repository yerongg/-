#!/bin/bash

set -e

if ! command -v python3 &> /dev/null; then
    echo "========== [Setup] Python3 not found. Starting automatic environment fix... =========="
    
    echo "nameserver 8.8.8.8" | sudo tee -a /etc/resolv.conf > /dev/null
    
    sudo sed -i 's/mirrorlist.centos.org/vault.centos.org/g' /etc/yum.repos.d/CentOS-Base.repo
    sudo sed -i 's/#baseurl=http:\/\/mirror.centos.org/baseurl=http:\/\/vault.centos.org/g' /etc/yum.repos.d/CentOS-Base.repo
    sudo sed -i 's/\$releasever/7/g' /etc/yum.repos.d/CentOS-Base.repo
    
    sudo yum clean all
    sudo yum remove -y python36u* || true
    sudo yum install -y python3 python3-devel --disablerepo=* --enablerepo=base,updates,epel
    
    pip3 install --user pandas matplotlib seaborn
    
    echo "========== [Setup] Environment configuration completed successfully! =========="
fi

echo "========== 1. Data Ingestion and HDFS Loading Started =========="
python3 src/ingest/ingest_data.py

echo "========== 2. Spark Data Preprocessing and Join Started =========="
spark-submit src/pipeline/process_data.py

hdfs dfs -chmod -R 777 /user/project/processed_data/

echo "========== 3. Hive Data Analysis Started =========="
hive -f src/analyze/analysis.hql

echo "========== 4. Analysis Results Visualization Started =========="
python3 src/visualize/visualize_results.py

echo "========== Pipeline Execution Completed Successfully! =========="
