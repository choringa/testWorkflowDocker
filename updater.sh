process=$(ps -aux | grep 'main.py' | awk '{split($0, a," "); print a[2]}' | head -1)
echo "1. Killing process id: " $process
kill -9 $process
echo "2. Pulling new code"
git -C /home/ubuntu/testWorkflowDocker pull
echo "3. Restart service"
python3 /home/ubuntu/testWorkflowDocker/main.py & 