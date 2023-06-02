import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from collections import deque

class BarberShopApp:
    def __init__(self, root): 
        self.root = root 
        self.root.title("Barber Shop")


        self.available_times = ["9:00 AM", "10:00 AM", "11:00 AM", "1:00 PM", "2:00 PM", "3:00 PM"] 
        self.available_capster = ["Ucup", "Adit"] 
        
        self.customer_name = tk.StringVar()
        self.customer_phone = tk.StringVar()
        self.selected_time = tk.StringVar()
        self.capster_request = tk.StringVar()

        self.image_path = "White Circular Barbershop Logo.png"  
        self.image = ImageTk.PhotoImage(Image.open(self.image_path))
        self.label_image = tk.Label(root, image=self.image)
        self.label_image.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

        self.label_name = tk.Label(root, text="Nama:")
        self.label_name.config(font=("Courier New", 12), fg="black")  
        self.label_name.grid(row=1, column=0, sticky=tk.W)
        self.entry_name = tk.Entry(root, textvariable=self.customer_name, width=30)
        self.entry_name.config(font=("Courier New", 12), fg="black", bg="white")
        self.entry_name.grid(row=1, column=1, columnspan=2)

        self.label_phone = tk.Label(root, text="No HP:")
        self.label_phone.config(font=("Courier New", 12), fg="black")  
        self.label_phone.grid(row=2, column=0, sticky=tk.W)
        self.entry_phone = tk.Entry(root, textvariable=self.customer_phone, width=30)
        self.entry_phone.config(font=("Courier New", 12), fg="black", bg="white")  
        self.entry_phone.grid(row=2, column=1, columnspan=2)

        self.label_time = tk.Label(root, text="Waktu:")
        self.label_time.config(font=("Courier New", 12), fg="black")  
        self.label_time.grid(row=3, column=0, sticky=tk.W)
        self.dropdown_time = tk.OptionMenu(root, self.selected_time, *self.available_times)
        self.dropdown_time.config(font=("Courier New", 12), fg="black", bg="white")  
        self.dropdown_time.grid(row=3, column=1, columnspan=2)

        self.label_capster = tk.Label(root, text="Capster yang diinginkan:")
        self.label_capster.config(font=("Courier New", 12), fg="black")  
        self.label_capster.grid(row=4, column=0, sticky=tk.W)
        self.dropdown_capster = tk.OptionMenu(root, self.capster_request, *self.available_capster)
        self.dropdown_capster.config(font=("Courier New", 12), fg="black", bg="white")  
        self.dropdown_capster.grid(row=4, column=1, columnspan=2)

        self.reserve_button = tk.Button(root, text="Reservasi", command=self.make_reservation)
        self.reserve_button.config(font=("Courier New", 14), bg="green", fg="white")  
        self.reserve_button.grid(row=5, column=0, columnspan=3, pady=10)

        self.reservation_stack = deque() #ucup
        self.reservation_queue = deque() #adit

    def make_reservation(self): 
        while True:
            customer_name = self.customer_name.get()
            customer_phone = self.customer_phone.get()
            selected_time = self.selected_time.get()
            capster_request = self.capster_request.get()

            if customer_name == "":
                messagebox.showerror("Error", "Mohon masukkan nama pelanggan.")
                return
            if customer_phone == "":
                messagebox.showerror("Error", "Mohon masukkan nomor telepon pelanggan.")
                return
            if not customer_phone.isdigit():
                messagebox.showerror("Error", "Nomor telepon harus berupa angka.")
                return
            if selected_time == "":
                messagebox.showerror("Error", "Mohon pilih waktu reservasi.")
                return
            if capster_request == "":
                messagebox.showerror("Error", "Mohon pilih capster yang tersedia.")
                return
            
            reservation = {
                "Nama": customer_name,
                "No HP": customer_phone,
                "Waktu": selected_time,
                "Capster yang diinginkan": capster_request
            }

            if capster_request == "Ucup":
                messagebox.showinfo("Reservasi Barbershop", "Reservasi berhasil! Capster yang diinginkan: Ucup")
                self.reservation_stack.append(reservation)  
            elif capster_request == "Adit":
                messagebox.showinfo("Reservasi Barbershop", "Reservasi berhasil! Capster yang diinginkan: Adit")
                self.reservation_queue.append(reservation) 

            self.show_reservation_info(reservation) 
            self.reset_input() 

            choice = messagebox.askyesno("Reservasi Barbershop", "Apakah Anda ingin melakukan reservasi lagi?")
            if not choice:
                break

        self.root.quit() 

    def show_reservation_info(self, reservation): 
        info_text = f"Informasi Reservasi:\n" \
                    f"Nama: {reservation['Nama']}\n" \
                    f"No HP: {reservation['No HP']}\n" \
                    f"Waktu: {reservation['Waktu']}\n" \
                    f"Capster yang diinginkan: {reservation['Capster yang diinginkan']}"
        messagebox.showinfo("Informasi Reservasi", info_text)

    def reset_input(self): #method
        self.customer_name.set("")
        self.customer_phone.set("")
        self.selected_time.set("")
        self.capster_request.set("")

root = tk.Tk()
app = BarberShopApp(root)
root.mainloop()
