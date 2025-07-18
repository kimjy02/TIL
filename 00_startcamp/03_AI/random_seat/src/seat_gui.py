import tkinter as tk
from tkinter import messagebox, scrolledtext
import random

# GUI 색상 테마
BG_COLOR = "#f6f5f3"  # 파스텔톤 배경
DESK_COLOR = "#ffffff"  # 흰색 책상
BORDER_COLOR = "#d1d1d1"
FONT = ("맑은 고딕", 11, "bold")

class SeatGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("랜덤 자리 배치")
        self.configure(bg=BG_COLOR)
        self.resizable(False, False)
        self.geometry("700x600")
        self.names = []
        self.seats = []
        self.create_widgets()

    def create_widgets(self):
        # 명단 입력
        tk.Label(self, text="명단을 한 줄에 한 명씩 입력하세요 (총 28명)", bg=BG_COLOR, font=("맑은 고딕", 10)).pack(pady=(20, 5))
        self.text_area = scrolledtext.ScrolledText(self, width=40, height=8, font=("맑은 고딕", 10))
        self.text_area.pack()
        tk.Button(self, text="자리 랜덤 배치", command=self.on_assign, font=FONT, bg="#b2d8d8", activebackground="#a3c9c9").pack(pady=10)
        self.seat_frame = tk.Frame(self, bg=BG_COLOR)
        self.seat_frame.pack(pady=10)
        self.draw_empty_seats()

    def draw_empty_seats(self):
        for widget in self.seat_frame.winfo_children():
            widget.destroy()
        # 칠판
        tk.Label(self.seat_frame, text="칠판", bg=BG_COLOR, font=("맑은 고딕", 13, "bold")).grid(row=0, column=0, columnspan=7, pady=(0, 18))
        # 4줄: 3+3
        for r in range(4):
            for c in range(3):
                tk.Label(self.seat_frame, text="", width=7, height=1, bg=DESK_COLOR, relief="ridge", bd=2).grid(row=r+1, column=c, padx=(8,2) if c==0 else (2,2), pady=4)
            tk.Label(self.seat_frame, text="", bg=BG_COLOR).grid(row=r+1, column=3, padx=8)
            for c in range(3):
                tk.Label(self.seat_frame, text="", width=7, height=1, bg=DESK_COLOR, relief="ridge", bd=2).grid(row=r+1, column=c+4, padx=(2,8) if c==2 else (2,2), pady=4)
        # 마지막 줄: 0,1,4,5번 위치에 책상
        for c in range(7):
            if c in [0,1,4,5]:
                tk.Label(self.seat_frame, text="", width=7, height=1, bg=DESK_COLOR, relief="ridge", bd=2).grid(row=5, column=c, padx=(8,2) if c==0 else (2,2), pady=4)
            else:
                tk.Label(self.seat_frame, text="", bg=BG_COLOR).grid(row=5, column=c, padx=8)

    def on_assign(self):
        names = [n.strip() for n in self.text_area.get("1.0", tk.END).splitlines() if n.strip()]
        if len(names) != 28:
            messagebox.showerror("오류", "명단은 28명이어야 합니다.")
            return
        random.shuffle(names)
        self.seats = []
        for i in range(4):
            left = names[i*6:i*6+3]
            right = names[i*6+3:i*6+6]
            self.seats.append([left, right])
        # 마지막 줄 4명은 따로 저장
        last_row = names[24:28]
        self.seats.append(last_row)
        self.draw_seats()

    def draw_seats(self):
        for widget in self.seat_frame.winfo_children():
            widget.destroy()
        tk.Label(self.seat_frame, text="칠판", bg=BG_COLOR, font=("맑은 고딕", 13, "bold")).grid(row=0, column=0, columnspan=7, pady=(0, 18))
        # 4줄: 3+3
        for r in range(4):
            left, right = self.seats[r]
            for c in range(3):
                name = left[c] if c < len(left) else ""
                tk.Label(self.seat_frame, text=name, width=7, height=1, bg=DESK_COLOR, relief="ridge", bd=2, font=FONT).grid(row=r+1, column=c, padx=(8,2) if c==0 else (2,2), pady=4)
            tk.Label(self.seat_frame, text="", bg=BG_COLOR).grid(row=r+1, column=3, padx=8)
            for c in range(3):
                name = right[c] if c < len(right) else ""
                tk.Label(self.seat_frame, text=name, width=7, height=1, bg=DESK_COLOR, relief="ridge", bd=2, font=FONT).grid(row=r+1, column=c+4, padx=(2,8) if c==2 else (2,2), pady=4)
        # 마지막 줄: 0,1,4,5번 위치에 학생 4명 순서대로 배치
        last_row = self.seats[4]
        for c in range(7):
            if c == 0:
                name = last_row[0] if len(last_row) > 0 else ""
                tk.Label(self.seat_frame, text=name, width=7, height=1, bg=DESK_COLOR, relief="ridge", bd=2, font=FONT).grid(row=5, column=0, padx=(8,2), pady=4)
            elif c == 1:
                name = last_row[1] if len(last_row) > 1 else ""
                tk.Label(self.seat_frame, text=name, width=7, height=1, bg=DESK_COLOR, relief="ridge", bd=2, font=FONT).grid(row=5, column=1, padx=(2,2), pady=4)
            elif c == 5:
                name = last_row[2] if len(last_row) > 2 else ""
                tk.Label(self.seat_frame, text=name, width=7, height=1, bg=DESK_COLOR, relief="ridge", bd=2, font=FONT).grid(row=5, column=4, padx=(2,2), pady=4)
            elif c == 6:
                name = last_row[3] if len(last_row) > 3 else ""
                tk.Label(self.seat_frame, text=name, width=7, height=1, bg=DESK_COLOR, relief="ridge", bd=2, font=FONT).grid(row=5, column=5, padx=(2,8), pady=4)
            else:
                tk.Label(self.seat_frame, text="", bg=BG_COLOR).grid(row=5, column=c, padx=8)

if __name__ == "__main__":
    app = SeatGUI()
    app.mainloop()
