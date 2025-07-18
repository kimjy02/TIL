
import tkinter as tk
from tkinter import messagebox, scrolledtext
import random
import os

BG_COLOR = "#f6f5f3"
CHEST_COLOR = "#ffffff"
BORDER_COLOR = "#d1d1d1"
FONT = ("맑은 고딕", 11, "bold")

class ChestGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("랜덤 사물함 배치")
        self.configure(bg=BG_COLOR)
        self.resizable(False, False)
        self.geometry("800x700")
        self.chests = []
        self.logo_img = None
        self.selected = []  # [(row, col), ...]
        self.chest_labels = []  # 2D 리스트: 각 칸의 Label 위젯
        self.edit_mode = False
        self.create_widgets()

    def create_widgets(self):
        # SSAFY 로고 이미지 첨부 코드 제거됨
        # 상단 타이틀
        tk.Label(self, text="사물함 자리 랜덤 배치", bg=BG_COLOR, fg="#3a3a3a", font=("맑은 고딕", 20, "bold")).pack(pady=(18, 6))
        # 안내문구
        tk.Label(self, text="명단을 한 줄에 한 명씩 입력하세요 (총 28명)", bg=BG_COLOR, fg="#4b6eaf", font=("맑은 고딕", 12, "bold")).pack(pady=(0, 8))
        self.text_area = scrolledtext.ScrolledText(self, width=40, height=8, font=("맑은 고딕", 11))
        self.text_area.pack(pady=(0, 8))
        btn_frame = tk.Frame(self, bg=BG_COLOR)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="사물함 랜덤 배치", command=self.on_assign, font=("맑은 고딕", 12, "bold"), bg="#b2d8d8", activebackground="#a3c9c9", relief="raised", bd=2).pack(side="left", padx=6)
        self.edit_btn = tk.Button(btn_frame, text="수정 모드", command=self.toggle_edit_mode, font=("맑은 고딕", 12, "bold"), bg="#f7c873", activebackground="#f7b733", relief="raised", bd=2)
        self.edit_btn.pack(side="left", padx=6)
        self.save_btn = tk.Button(btn_frame, text="수정 완료(텍스트 저장)", command=self.save_as_text, font=("맑은 고딕", 12, "bold"), bg="#b2e6b2", activebackground="#8fd88f", relief="raised", bd=2, state="disabled")
        self.save_btn.pack(side="left", padx=6)
        self.edit_label = tk.Label(self, text="", bg=BG_COLOR, fg="#d17b00", font=("맑은 고딕", 11, "bold"))
        self.edit_label.pack()
        self.exchange_label = tk.Label(self, text="", bg=BG_COLOR, fg="#1976d2", font=("맑은 고딕", 11, "bold"))
        self.exchange_label.pack()
        self.chest_frame = tk.Frame(self, bg=BG_COLOR)
        self.chest_frame.pack(pady=18)
        self.draw_empty_chests()

    def draw_empty_chests(self):
        for widget in self.chest_frame.winfo_children():
            widget.destroy()
        self.chest_labels = []
        for r in range(4):
            row_labels = []
            for c in range(7):
                lbl = tk.Label(
                    self.chest_frame,
                    text="",
                    width=6, height=2,
                    bg=CHEST_COLOR,
                    relief="ridge",
                    bd=2
                )
                lbl.grid(row=r, column=c, padx=0, pady=0)
                row_labels.append(lbl)
            self.chest_labels.append(row_labels)

    def on_assign(self):
        names = [n.strip() for n in self.text_area.get("1.0", tk.END).splitlines() if n.strip()]
        if len(names) != 28:
            messagebox.showerror("오류", "명단은 28명이어야 합니다.")
            return
        random.shuffle(names)
        self.chests = []
        for i in range(4):
            self.chests.append(names[i*7:(i+1)*7])
        self.draw_chests()

    def draw_chests(self):
        for widget in self.chest_frame.winfo_children():
            widget.destroy()
        self.chest_labels = []
        for r in range(4):
            row_labels = []
            for c in range(7):
                idx = r*7 + c + 1
                name = self.chests[r][c] if r < len(self.chests) and c < len(self.chests[r]) else ""
                label_text = f"{idx}\n{name}"
                lbl = tk.Label(
                    self.chest_frame,
                    text=label_text,
                    width=6, height=2,
                    bg=CHEST_COLOR,
                    relief="ridge",
                    bd=2,
                    font=("맑은 고딕", 13, "bold"),
                    fg="#2d3a4a"
                )
                lbl.grid(row=r, column=c, padx=0, pady=0)
                if self.edit_mode:
                    lbl.bind('<Button-1>', lambda e, row=r, col=c: self.on_chest_click(row, col))
                row_labels.append(lbl)
            self.chest_labels.append(row_labels)
    def toggle_edit_mode(self):
        self.edit_mode = not self.edit_mode
        if self.edit_mode:
            self.edit_label.config(text="수정 모드: 교환할 두 칸을 차례로 클릭하세요.")
            self.exchange_label.config(text="두 칸을 차례로 클릭하면 1:1 교환됩니다.")
            self.save_btn.config(state="normal")
            self.edit_btn.config(text="수정 취소")
        else:
            self.edit_label.config(text="")
            self.exchange_label.config(text="")
            self.save_btn.config(state="disabled")
            self.edit_btn.config(text="수정 모드")
            self.selected.clear()
        self.draw_chests()

    def on_chest_click(self, row, col):
        if not self.edit_mode:
            return
        if len(self.selected) == 0:
            self.selected.append((row, col))
            self.chest_labels[row][col].config(bg="#ffe082")
        elif len(self.selected) == 1:
            r1, c1 = self.selected[0]
            r2, c2 = row, col
            if (r1, c1) == (r2, c2):
                self.chest_labels[r1][c1].config(bg=CHEST_COLOR)
                self.selected.clear()
                return
            # swap
            self.chests[r1][c1], self.chests[r2][c2] = self.chests[r2][c2], self.chests[r1][c1]
            self.selected.clear()
            self.draw_chests()

    def save_as_text(self):
        # 수정 모드 종료 및 칸 색상 복원
        if self.edit_mode:
            self.edit_mode = False
            self.edit_label.config(text="")
            self.save_btn.config(state="disabled")
            self.edit_btn.config(text="수정 모드")
            self.selected.clear()
            self.draw_chests()
            self.update()
        # 저장 폴더 생성
        output_dir = os.path.join(os.path.dirname(__file__), '../사물함_배치_완료')
        os.makedirs(output_dir, exist_ok=True)
        # 파일명 입력
        from tkinter.simpledialog import askstring
        from datetime import datetime
        default_name = f"chest_result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        filename = askstring("파일명 입력", "저장할 파일 이름을 입력하세요:", initialvalue=default_name)
        if not filename:
            return
        if not filename.lower().endswith('.txt'):
            filename += '.txt'
        save_path = os.path.join(output_dir, filename)
        try:
            with open(save_path, "w", encoding="utf-8") as f:
                for r in range(4):
                    for c in range(7):
                        idx = r*7 + c + 1
                        name = self.chests[r][c] if r < len(self.chests) and c < len(self.chests[r]) else ""
                        f.write(f"{idx:2}: {name}\t")
                    f.write("\n")
            messagebox.showinfo("저장 완료", f"사물함 배치 결과가\n{save_path}\n으로 저장되었습니다.")
        except Exception as e:
            messagebox.showerror("오류", f"저장 중 오류 발생: {e}")

if __name__ == "__main__":
    app = ChestGUI()
    app.mainloop()
