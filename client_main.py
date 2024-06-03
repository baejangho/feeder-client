import tkinter as tk
from feeder_client import Feeder_client

## 실제 급이시 False로 변경 ##
sim = True

# Feeder_client 객체를 생성합니다.
server_ip = '127.0.0.1' # server ip
# server_ip = '192.168.0.4'
Feeder_01 = Feeder_client(server_ip,2200,2201)


# Tk 객체를 생성합니다.
root = tk.Tk()

# state_msg 딕셔너리의 각 키에 대해 StringVar 객체와 Label 위젯을 생성합니다.
label_vars = {}
for i, key in enumerate(Feeder_01.state_msg.keys()):
    label_var = tk.StringVar()
    label_vars[key] = label_var

    key_label = tk.Label(root, text=key)
    key_label.grid(row=i, column=0)

    value_label = tk.Label(root, textvariable=label_var)
    value_label.grid(row=i, column=1)



def update_labels():
    # state_msg 딕셔너리의 각 키-값 쌍에 대해 StringVar 객체의 값을 업데이트합니다.
    #print(Feeder_01.state_msg)
    for key, value in Feeder_01.state_msg.items():
        label_vars[key].set(value)

    # 200ms 후에 이 함수를 다시 호출합니다.
    root.after(200, update_labels)

# update_labels 함수를 호출합니다.
update_labels()

def on_closing():
    print("Window is closing")
    if sim == False:
        Feeder_01.ML.terminate()
    root.destroy()

# UI를 실행합니다.
try:
    root.protocol("WM_DELETE_WINDOW", on_closing)
    update_labels()
    root.mainloop()
except KeyboardInterrupt:
    print('사용자종료') 
    #Feeder_01.motor.terminate()
    #Feeder_01.loadcell.terminate()  
    root.destroy()
    
