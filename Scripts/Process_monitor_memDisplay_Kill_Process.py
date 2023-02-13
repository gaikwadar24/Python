import psutil

def get_processes():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        processes.append(proc)
    return processes

def kill_process(pid):
    try:
        process = psutil.Process(pid)
        process.kill()
        print(f"Process with PID {pid} has been successfully killed.")
    except Exception as e:
        print(f"An error occurred while trying to kill process with PID {pid}: {e}")

def main():
    processes = get_processes()
    for process in processes:
        if process.info['memory_info'] and process.info['name'] != 'System' and process.info['memory_info'].rss > 100000000:
            print(f"Process with PID {process.info['pid']} and name {process.info['name']} is using {process.info['memory_info'].rss} bytes of memory.")
            user_input = input(f"Do you want to kill this process? (y/n)")
            if user_input == 'y':
                kill_process(process.info['pid'])


if __name__ =="__main__":
    main()
