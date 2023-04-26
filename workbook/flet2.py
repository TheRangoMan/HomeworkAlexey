import flet
from flet import Row, icons,IconButton, TextField, Page, TextStyle, TextButton

def main(page:Page):
    page.title = "Counter App"
    page.vertical_alignment = "center" 
    
    
    def minus(e):
        if textfield.text != '0' and textfield.text!=0:
            textfield.text = int(textfield.text)-1
        page.update()
    
    def plus(e):
        textfield.text = int(textfield.text)+1
        page.update()
        
    def focus_my(e):
        textfield.color = "RED"
        page.update()
        
    def blur_my(e):
        textfield.color = "BLUE"
        page.update()
        
    
    textfield = TextButton( text = '0', width=100, on_focus=focus_my,on_blur=blur_my)      
    
    page.add(
        Row(
            [
                IconButton(icons.REMOVE, on_click=minus), 
                textfield,
                IconButton(icons.ADD, on_click=plus)
            ],
            alignment='center'
        )
    )
    
    
    
    
    
flet.app(target=main, view = flet.WEB_BROWSER)
    
    