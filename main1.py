import flet as ft
import requests

def main(page: ft.Page):
    page.title = "Погодная программа"
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    user_data = ft.TextField(label='Введите город', width=400)
    weather_data = ft.Text('')

    def get_info(e):
        if len(user_data.value) < 2:
            return

        API = 'dff38c44fe5c471db1891432240905'
        URL = f'https://api.weatherapi.com/v1/current.json?key={API}&q={user_data.value}&aqi=no'
        res = requests.get(URL).json()
        temp = res['current']['temp_c']
        weather_data.value = 'Температура: ' + str(temp) + 'C`'
        page.update()
        
    def change_theme(e):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.SUNNY, on_click=change_theme),
                ft.Text('Погодная программа')
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([user_data], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([weather_data], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.ElevatedButton(text='Получить температуру', on_click=get_info)],
               alignment=ft.MainAxisAlignment.CENTER)
    )


ft.app(target=main, view=ft.AppView.WEB_BROWSER)