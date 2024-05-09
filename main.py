import flet as ft


def main(page: ft.Page):
    page.title = "Jopa"
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    user_label = ft.Text('Zdarova')
    user_text = ft.TextField(value='0', width=150, text_align=ft.TextAlign.CENTER)

    def get_info(e):
        user_label.value = user_text.value
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.HOME, on_click=get_info),
                ft.Icon(ft.icons.BACK_HAND),
                ft.ElevatedButton(text='Push', on_click=get_info)

            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                user_label,
                user_text,

            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
    )


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
