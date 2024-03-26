kill -9 $(ps -aux | grep 'main.py' | awk '{split($0, a," "); print a[2]}' | head -1)
git -C /home/ubuntu/testWorkflowDocker pull
python3 /home/ubuntu/testWorkflowDocker/main.py & 