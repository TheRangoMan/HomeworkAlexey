import flet as ft 
from flet import Page, IconButton, Text, TextField, icons

def main(page:Page):
    #page.vertical_alignment='center'
    page.horizontal_alignment='center'
    def submityear(e):
        try:
            _ = int(yearText.value)
            monthText.focus()
        except:
            page.dialog = dlg
            dlg.open=True
            yearText.focus()
            page.update()
    
    def submitmonth(e):
        businessText.focus()
        
    
    def submitbusiness(e):
        incomeText.focus()
        
    def close_dlg(e):
        dlg.open = False
        page.update() 
     
     
    dlg = ft.AlertDialog( modal=True,
                         title=ft.Text("Data Error!"), 
                         content=ft.Text("Please check format of your data"),
                         actions=[ft.TextButton("OK",on_click=close_dlg)])     
         
        
        
    yearLabel = Text("Year: ", color=ft.colors.RED, size=40)
    yearText = TextField(value="",color=ft.colors.BLUE, text_size=40, on_submit=submityear)
    yearRow = ft.Row([yearLabel, yearText],vertical_alignment='center')
    
    monthLabel = Text("Month: ", color=ft.colors.RED, size=40)
    monthText = TextField(value="",color=ft.colors.BLUE, text_size=40,on_submit=submitmonth)
    monthrRow = ft.Row([monthLabel, monthText],vertical_alignment='center')
    
    businessLabel = Text("Business: ", color=ft.colors.RED, size=40)
    businessText = TextField(value="",color=ft.colors.BLUE, text_size=40,on_submit=submitbusiness)
    businessrRow = ft.Row([businessLabel, businessText],vertical_alignment='center')
    
    incomeLabel = Text("Income: ", color=ft.colors.RED, size=40)
    incomeText = TextField(value="",color=ft.colors.BLUE, text_size=40)
    incomeRow = ft.Row([incomeLabel, incomeText],vertical_alignment='center')
    
    page.add(ft.Column([yearRow,monthrRow,businessrRow,incomeRow],horizontal_alignment='center'))
    
ft.app(target=main)