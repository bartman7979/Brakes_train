import math
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Color, RoundedRectangle, Rectangle
from kivy.core.window import Window

class GradientButton(Button):
    def __init__(self, **kwargs):
        super(GradientButton, self).__init__(**kwargs)
        with self.canvas.before:
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(pos=self.update_rect, size=self.update_rect)
            self.bind(on_press=self.on_press)
        Window.bind(on_resize=self.on_window_resize)

    def on_press(self, *args):
        with self.canvas.before:
            self.canvas.before.clear()
            Color(0, 0, 0, 0.1)  # Red
            self.rect = Rectangle(size=self.size, pos=self.pos)
            Color(1, 1, 1, 1)  # Blue
            self.rect = Rectangle(size=self.size, pos=self.pos)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_window_resize(self, window, width, height):
        self.font_size = width * 0.05  # Размер шрифта будет 5% от ширины окна

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        btn = GradientButton(text='Gradient Button', size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(btn)
        return layout

class TrainPressureApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        with self.layout.canvas.before:
            self.bg = Image(source='D:/PyThon/Kivy2/444.png', allow_stretch=True, keep_ratio=False, size=self.layout.size, pos=self.layout.pos)
            self.layout.bind(size=self.update_bg, pos=self.update_bg)
        self.weight_input = self.create_anchor_layout(TextInput(hint_text='Введите вес поезда', multiline=False, background_color=(1, 1, 1, 0.9), font_size=20, size_hint=(1, None), height=50))
        self.axis_l_input = self.create_anchor_layout(TextInput(hint_text='Введите оси: 3.5 Т.с', multiline=False, background_color=(1, 1, 1, 0.9), font_size=20, size_hint=(1, None), height=50))
        self.axis_l_b_input = self.create_anchor_layout(TextInput(hint_text='Введите оси: 5 Т.с', multiline=False, background_color=(1, 1, 1, 0.9), font_size=20, size_hint=(1, None), height=50))
        self.axis_b_input = self.create_anchor_layout(TextInput(hint_text='Введите оси: 7 Т.с', multiline=False, background_color=(1, 1, 1, 0.9), font_size=20, size_hint=(1, None), height=50))
        self.axis_bb_input = self.create_anchor_layout(TextInput(hint_text='Введите оси: 8.5 Т.с', multiline=False, background_color=(1, 1, 1, 0.9), font_size=20, size_hint=(1, None), height=50))
        self.axis_p_input = self.create_anchor_layout(TextInput(hint_text='Введите оси: 10 Т.с', multiline=False, background_color=(1, 1, 1, 0.9), font_size=20, size_hint=(1, None), height=50))


        self.result_label = Label(text='Результаты:', font_size=20, size_hint=(1, None), height=100)

        self.empty_button = GradientButton(text='Порожний', font_size=18, size_hint=(0.33, None), height=50)
        self.medium_button = GradientButton(text='Средний', font_size=18, size_hint=(0.33, None), height=50)
        self.loaded_button = GradientButton(text='Груженый', font_size=18, size_hint=(0.33, None), height=50)

        self.empty_button.bind(on_press=self.set_train_type)
        self.medium_button.bind(on_press=self.set_train_type)
        self.loaded_button.bind(on_press=self.set_train_type)

        self.calculate_button = GradientButton(
            text='Рассчитать',
            font_size=18,
            size_hint=(1, None),
            height=50,
            color=(1, 1, 1, 1)  # Цвет текста
        )
        self.calculate_button.bind(on_press=self.calculate)

        self.button_layout = BoxLayout(orientation='horizontal', size_hint=(1, None), height=50)
        self.button_layout.add_widget(self.empty_button)
        self.button_layout.add_widget(self.medium_button)
        self.button_layout.add_widget(self.loaded_button)

        self.layout.add_widget(self.weight_input)
        self.layout.add_widget(self.axis_l_input)
        self.layout.add_widget(self.axis_l_b_input)
        self.layout.add_widget(self.axis_b_input)
        self.layout.add_widget(self.axis_bb_input)
        self.layout.add_widget(self.axis_p_input)
        self.layout.add_widget(self.button_layout)
        self.layout.add_widget(self.calculate_button)
        self.layout.add_widget(self.result_label)

        Window.bind(on_resize=self.on_window_resize)

        return self.layout

    def create_anchor_layout(self, widget):
        layout = AnchorLayout()
        layout.add_widget(widget)
        return layout

    def get_text_from_anchor_layout(self, anchor_layout):
        for child in anchor_layout.children:
            if isinstance(child, TextInput):
                return child.text
        return ""

    def calculate(self, instance):
        weight_text = self.get_text_from_anchor_layout(self.weight_input)
        axis_l_text = self.get_text_from_anchor_layout(self.axis_l_input)
        axis_l_b_text = self.get_text_from_anchor_layout(self.axis_l_b_input)
        axis_b_text = self.get_text_from_anchor_layout(self.axis_b_input)
        axis_bb_text = self.get_text_from_anchor_layout(self.axis_bb_input)
        axis_p_text = self.get_text_from_anchor_layout(self.axis_p_input)

        weight = float(weight_text) if weight_text else 0
        axis_l = float(axis_l_text) if axis_l_text else 0
        axis_l_b = float(axis_l_b_text) if axis_l_b_text else 0
        axis_b = float(axis_b_text) if axis_b_text else 0
        axis_bb = float(axis_bb_text) if axis_bb_text else 0
        axis_p = float(axis_p_text) if axis_p_text else 0

        if self.train_type == 'порожний':
            factor = 0.33
        elif self.train_type == 'средний':
            factor = 0.44
        elif self.train_type == 'груженый':
            factor = 0.55
        else:
            self.result_label.text = 'Неверный тип поезда'
            return

        p = math.ceil(self.pressure(weight, factor))
        s = math.ceil(self.pressure(weight, 0.006))
        osi = self.pressure3(axis_l, axis_b, axis_p, axis_l_b, axis_bb)

        self.result_label.text = f'Требуемое нажатие: {p} тс.\nКол-во ручных тормозов в осях: {s}\nФактическое нажатие: {osi} тс.'


    def create_anchor_layout(self, widget):
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center')
        anchor_layout.add_widget(widget)
        return anchor_layout

    def update_bg(self, instance, value):
        self.bg.size = instance.size
        self.bg.pos = instance.pos

    def on_window_resize(self, window, width, height):
        font_size = width * 0.05  # Размер шрифта будет 5% от ширины окна
        self.weight_input.font_size = font_size
        self.axis_l_input.font_size = font_size
        self.axis_l_b_input.font_size = font_size
        self.axis_b_input.font_size = font_size
        self.axis_bb_input.font_size = font_size
        self.axis_p_input.font_size = font_size
        self.result_label.font_size = font_size

    def set_train_type(self, instance):
        self.train_type = instance.text.lower()

    def pressure(self, weight, factor):
        return round(weight * factor, 1)

    def pressure3(self, axis_l, axis_b, axis_p, axis_l_b, axis_bb):
        rounded_l = math.ceil(axis_l * 3.5)
        rounded_l_b = math.ceil(axis_l_b * 5)
        rounded_b = math.ceil(axis_b * 7)
        rounded_bb = math.ceil(axis_bb * 8.5)
        rounded_p = math.ceil(axis_p * 10)
        result = rounded_l + rounded_b + rounded_p + rounded_l_b + rounded_bb
        return result

    def update_bg(self, *args):
        self.bg.size = self.layout.size
        self.bg.pos = self.layout.pos

if __name__ == '__main__':
    TrainPressureApp().run()